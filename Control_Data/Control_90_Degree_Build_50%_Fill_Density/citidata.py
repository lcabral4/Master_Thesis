
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 13:45:24 2021

@author: lcabral4
"""

#!/usr/bin/env python3
import numpy as np
import sys

PY3 = (sys.version_info.major == 3)

class CITIPackage(object):
    def __init__(self):
        self.name = None
        self.constants = {}
        self.citi_version = None
        self.comments = []
        self.dep_names = []
        self.deps = {}
        self.indep_name = None
        self.indep_format = None
        self.indep = None
        self.segments = []

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        s = ["CITI Package named '%s'" % self.name]
        if self.indep is not None:
            s.append("indep: %s (%u values)" % (self.indep_name, len(self.indep)))
        for dname, d in self.deps.items():
            if d['data'] is not None:
                s.append( ("dep: %s (%u values)" % (dname, len(d['data']))) )
            else:
                s.append("No data for dep '%s'!" % dname)
        return "\n".join(s)

class CITIFile(object):
    def __init__(self, fname):
        self.packages = []
        self.comments = []
        if PY3:
            with open(fname, 'r', encoding='utf-8', errors='ignore') as fh:
                self.lines = fh.readlines()
                self._parselines()
        else:
            with open(fname, 'r') as fh:
                self.lines = fh.readlines()
                self._parselines()

    def _parselines(self):
        package = None
        for line in self.lines:
            #skip empty lines
            if len(line.strip()) == 0:
                continue
#            print("parsing line %s"% line)
            if line.strip().startswith('#'):
                # ignore dev-specific vars for now
                continue
            line_parts = line.strip().split(' ', 1)
            keyword = line_parts[0]
            if len(line_parts) > 1:
                rest_of_line = line_parts[1]
            else:
                rest_of_line = ""
            if keyword == "CITIFILE":
                #begins a new CITI package
                if isinstance(package, CITIPackage):
                    self.packages.append(package)
                package = CITIPackage()
                data_segment_counter = 0
                package.citi_version = rest_of_line
            elif keyword == "NAME":
                package.name = rest_of_line
            elif keyword == "COMMENT":
                #some files might have comments before the CITIFILE header starts. we add them to CITIFile object.
                if not isinstance(package, CITIPackage):
                    self.comments.append(rest_of_line)
                else:
                    package.comments.append(rest_of_line)
            elif keyword == "CONSTANT":
                name, value = rest_of_line.split(' ', 1)
                package.constants[name] = value
            elif keyword == "VAR":
                #defines name, format and npoints of indep
                indep_name, indep_format, indep_npoints = rest_of_line.split(' ')
                package.indep_name = indep_name
                package.indep_format = indep_format
                package.indep_npoints = int(indep_npoints)
            elif keyword == "DATA":
                #defines a dependent variable
                name, frmt = rest_of_line.split(' ', 1)
                package.dep_names.append(name) # keep track of sequence
                package.deps[name] = {'format': frmt,
                                     'unit': None,
                                     'data': None}
            elif keyword == "VAR_LIST_BEGIN":
                parts = rest_of_line.split(' ', 1)
                if len(parts) > 1:
                    name, unit = parts
                else:
                    name = parts[0]
                    unit = ""
                package.indep_unit = unit
                collector = []
            elif keyword == "VAR_LIST_END":
                package.indep = np.fromiter(collector, np.float)
                collector = []
            elif keyword == "SEG_LIST_BEGIN":
                collector = []
            elif keyword == "SEG_LIST_END":
                package.segments.append(rest_of_line)
                collector = []
            elif keyword == "BEGIN":
                parts = rest_of_line.split(' ', 1)
                if len(parts) > 1:
                    dep_name, unit = parts
                else:
                    dep_name = parts[0]
                    unit = ""
                if not dep_name: # if not supplied in line we have to rely on sequence and header
                    dep_name = package.dep_names[data_segment_counter]
                package.deps[dep_name]['unit'] = unit
                pass
            elif keyword == "END":
                frmt = package.deps[dep_name]['format']
                if frmt == "MAG":
                    package.deps[dep_name]['data'] = np.fromiter(collector, np.float)
                elif frmt == "RI":
                    allvals = ','.join(collector)
                    data = np.fromstring(allvals, dtype=np.float, sep=',', count=2*len(collector)).reshape(-1,2)
                    data = data[:,0]+ 1j*data[:,1]
                    package.deps[dep_name]['data'] = data
                elif frmt == "MAGANGLE":
                    allvals = ','.join(collector)
                    data = np.fromstring(allvals, dtype=np.float, sep=',', count=2*len(collector)).reshape(-1,2)
                    data = data[:,0] * np.exp(1j*data[:,1]*np.pi/180.0*np.pi/180.0)
                    package.deps[dep_name]['data'] = data
                collector = []
                data_segment_counter += 1
            else: # only one word in line, unknown keyword or data
                collector.append(line.strip())

        if isinstance(package, CITIPackage):
            self.packages.append(package)

    def __str__(self):
        return ("CITI data object with %u data packages." % len(self.packages))

def genfromfile(fname):
    return CITIFile(fname)


if __name__=="__main__":
    for fname in sys.argv[1:]:
        print("parsing file %s" % fname)
        c = genfromfile(fname)
        for p in c.packages:
            print(p.name)
            print(p.citi_version)
            for c,v in p.constants.items():
                print("%s = %s" % (c,v))
            print(p)
            print("package name %s" % p.name)
            print("found INDEP %s" % (p.indep_name))
            print(p.indep)
            for dname, d in p.deps.items():
                print("found DEP %s %s %s" % (dname, d['format'], d['unit']))
            print(d['data'])