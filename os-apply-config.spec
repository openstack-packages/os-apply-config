Name:		os-apply-config
Version:	0.1.12
Release:	3%{?dist}
Summary:	Configure files from cloud metadata

License:	ASL 2.0
URL:		http://pypi.python.org/pypi/%{name}
Source0:	http://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python2-devel
BuildRequires:	python-setuptools
BuildRequires:	python-pbr

Requires:	python-setuptools
Requires:	python-argparse
Requires:	python-anyjson
Requires:	pystache

%description
Tool to apply openstack heat metadata to files on the system.

%prep

%setup -q -n %{name}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc README.rst
%doc LICENSE
%{_bindir}/os-apply-config
%{_bindir}/os-config-applier
%{python_sitelib}/os_apply_config*

%changelog
* Mon Feb 24 2014 Steven Dake <sdake@redhat.com> - 0.1.12-3
- Override python-pbr rquires by manually sedding the release and version
- Add pystache requires from bodhi testing

* Fri Feb 21 2014 Steven Dake <sdake@redhat.com> - 0.1.12-2
- Add python-pbr buildrequires

* Wed Feb 19 2014 Steven Dake <sdake@redhat.com>  - 0.1.12-1
- Update to version 0.1.12
- Add python2-devel buildrequires

* Tue Oct 15 2013 Lucas Alvares Gomes <lgomes@redhat.com> - 0.1.2-1
- Update to version 0.1.2

* Thu Sep 5 2013 Lucas Alvares Gomes <lgomes@redhat.com> - 0.0.1-1
- Initial version
