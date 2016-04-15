Name:		os-apply-config
Version:	XXX
Release:	XXX
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
Requires:       python-six >= 1.9.0
Requires:       python-pbr
Requires:       python-six

%description
Tool to apply openstack heat metadata to files on the system.

#
# patches_base: 0.1.16
#

%prep
%setup -q -n %{name}-%{upstream_version}


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
