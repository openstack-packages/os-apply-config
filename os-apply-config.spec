%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:		os-apply-config
Version:	0.1.32
Release:	4%{?dist}
Summary:	Configure files from cloud metadata

License:	ASL 2.0
URL:		http://pypi.python.org/pypi/%{name}
Source0:	http://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python2-devel
BuildRequires:	python-setuptools
BuildRequires:	python-pbr

Requires:	python-pbr
Requires:	python-setuptools
Requires:	python-argparse
Requires:	python-anyjson
Requires:	pystache
Requires:	python-six >= 1.9.0

%description
Tool to apply openstack heat metadata to files on the system.

%prep
%setup -q -n %{name}-%{upstream_version}


%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc README.rst
%doc LICENSE
%{_bindir}/os-apply-config
%{_bindir}/os-config-applier
%{python2_sitelib}/os_apply_config*

%changelog
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 20 2015 James Slagle <jslagle@redhat.com> 0.1.32-3
- Add Requires: python-pbr

* Tue Oct 20 2015 James Slagle <jslagle@redhat.com> 0.1.32-2
- Remove 0001-Remove-pbr-runtime-dependency-and-replace-with-build.patch

* Tue Oct 20 2015 James Slagle <jslagle@redhat.com> 0.1.32-1
- Update to upstream 0.1.32

* Tue Oct 28 2014 James Slagle <jslagle@redhat.com> 0.1.23-1
- Update to upstream 0.1.23

* Fri Sep 12 2014 James Slagle <jslagle@redhat.com> 0.1.21-1
- Update to upstream 0.1.21

* Thu Sep 11 2014 James Slagle <jslagle@redhat.com> - 0.1.16-3
- Switch to rdopkg

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 9 2014 Ben Nemec <bnemec@redhat.com> - 0.1.16-1
- Update to version 0.1.16

* Mon Feb 24 2014 Steven Dake <sdake@redhat.com> - 0.1.12-5
- Add patch file to spec missing in -4

* Mon Feb 24 2014 Steven Dake <sdake@redhat.com> - 0.1.12-4
- Add sed logic for python-pbr requires

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
