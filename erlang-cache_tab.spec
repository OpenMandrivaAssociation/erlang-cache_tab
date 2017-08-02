%global srcname cache_tab
# Erlang packages don't seem to ship debug files, as the build process does not generate them
%global debug_package %{nil}


Name: erlang-cache_tab
Version: 1.0.4
Release: %mkrel 1
Group:   Development/Erlang
Summary: Erlang cache table application

License: ASL 2.0
URL: https://github.com/processone/cache_tab/
Source0: https://github.com/processone/cache_tab/archive/%{version}.tar.gz

BuildRequires: erlang-rebar
BuildRequires: erlang-p1_utils


%description
This application is intended to proxy back-end operations for Key-Value insert,
lookup and delete and maintain a cache of those Key-Values in-memory, to save
back-end operations. Operations are intended to be atomic between back-end and
cache tables. The lifetime of the cache object and the max size of the cache
can be defined as table parameters to limit the size of the in-memory tables.


%prep
%autosetup -n cache_tab-%{version}


%build
%rebar_compile


%install
install -p -D -m 644 ebin/* --target-directory=$RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/ebin


%files
%license LICENSE.txt
%doc CHANGELOG.md
%doc README.md
%{_erllibdir}/%{srcname}-%{version}



%changelog
* Thu Nov 17 2016 neoclust <neoclust> 1.0.4-1.mga6
+ Revision: 1068003
- New version 1.0.4

* Fri May 06 2016 neoclust <neoclust> 1.0.1-2.mga6
+ Revision: 1009829
- imported package erlang-cache_tab

