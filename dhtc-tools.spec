Summary: A collection of tools for collecting and visualizing HTCondor data 
Name: dhtc-tools
Version: 1.0.0
Release: 1
License: MIT
Group: System Environment/Daemons
URL: http://dhtc.io
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: python-futures python-argparse

%description
The Distributed High Throughput Computing Tools are a collection of tools for collecting real-time and historical data from HTCondor on the Open Science Grid and visualizing that data. 

%package condor-retrieval
Group: System Environment/Daemons
Summary: Tool for collecting real-time data from HTCondor collectors
%description condor-retrieval
The condor_retrieval.py program polls HTCondor collectors for data and inputs the data into a Mongo database.

%package condor-job-table
Group: System Environment/Daemons
Summary: Job table for real-time HTCondor data
%description condor-job-table
The job table helps visualize the real-time data retrieved from the condor_retrieval.py program. 

%package condor-history-probe
Group: System Environment/Daemons
Summary: Tool for collecting historical data from HTCondor
%description condor-history-probe
The HTCondor history probe stores condor job history in a database for analytics.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datarootdir} $RPM_BUILD_ROOT/%{_sysconfdir}/condor_retrieval $RPM_BUILD_ROOT/%{_initddir} $RPM_BUILD_ROOT/%{_bindir}
cp condor-retrieval/condor_retrieval.py $RPM_BUILD_ROOT/%{_bindir}/condor_retrieval.py
cp condor-retrieval/config.ini $RPM_BUILD_ROOT/%{_sysconfdir}/condor_retrieval/config.ini
cp condor-retrieval/condor-retrieval $RPM_BUILD_ROOT/%{_initddir}/condor-retrieval
cp -r condor-job-table $RPM_BUILD_ROOT/%{_datarootdir}/condor-job-table
cp condor-history-probe/probe_history $RPM_BUILD_ROOT/%{_bindir}/probe_history
cp condor-history-probe/condor-probe-cron $RPM_BUILD_ROOT/%{_initddir}/condor-probe-cron

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc

%files condor-retrieval
%{_bindir}/condor_retrieval.py
%{_sysconfdir}/condor_retrieval/config.ini
%{_initddir}/condor-retrieval

%files condor-job-table
%{_datarootdir}/condor-job-table

%files condor-history-probe
%{_bindir}/probe_history
%{_initddir}/condor-probe-cron

%changelog
* Wed Jul 30 2014 Anton Yu <antonyu@login01.osgconnect.net> - 1.0.0-1
- Initial build.

