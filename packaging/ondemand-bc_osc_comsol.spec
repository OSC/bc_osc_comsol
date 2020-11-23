# Disable debuginfo as it causes issues with bundled gems that build libraries
%global debug_package %{nil}
%global repo_name bc_osc_comsol
%global app_name bc_osc_comsol
%{!?package_version: %define package_version %{major}.%{minor}.%{patch}}
%{!?package_release: %define package_release 1}
%{!?git_tag: %define git_tag v%{package_version}}
%define git_tag_minus_v %(echo %{git_tag} | sed -r 's/^v//')

Name:     ondemand-%{app_name}
Version:  %{package_version}
Release:  %{package_release}%{?dist}
Summary:  Batch Connect - OSC COMSOL Multiphysics

Group:    System Environment/Daemons
License:  MIT
URL:      https://github.com/OSC/%{repo_name}
Source0:  https://github.com/OSC/%{repo_name}/archive/%{git_tag}.tar.gz

Requires: ondemand

# Disable automatic dependencies as it causes issues with bundled gems and
# node.js packages used in the apps
AutoReqProv: no

%description
A Batch Connect app designed for OSC OnDemand that launches COMSOL Multiphysics within an Owens batch job.


%prep
%setup -q -n %{repo_name}-%{git_tag_minus_v}


%build


%install
export PASSENGER_APP_ENV=production
export PASSENGER_BASE_URI=/pun/sys/%{app_name}
mkdir -p %{buildroot}%{_localstatedir}/www/ood/apps/sys/%{app_name}
if [ -x bin/setup ]; then
    bin/setup
fi
cp -a ./. %{buildroot}%{_localstatedir}/www/ood/apps/sys/%{app_name}/
echo v%{version} > %{buildroot}%{_localstatedir}/www/ood/apps/sys/%{app_name}/VERSION

%files
%defattr(-,root,root)
%{_localstatedir}/www/ood/apps/sys/%{app_name}
%{_localstatedir}/www/ood/apps/sys/%{app_name}/manifest.yml


%changelog
* Mon Oct 22 2018 Morgan Rodgers <mrodgers@osc.edu> 0.4.0-1
- Update COMSOL multiphysics to v0.4.0 (mrodgers@osc.edu)

* Wed Mar 21 2018 Jeremy Nicklas <jnicklas@osc.edu> 0.3.0-1
- Bump bc_osc_comsol to 0.3.0 (jnicklas@osc.edu)
- Remove old version (tdockendorf@osc.edu)

* Tue Mar 13 2018 Trey Dockendorf <tdockendorf@osc.edu> 0.2.0-1
- Upgrade ondemand-bc_osc_comsol back to 0.2.0 (tdockendorf@osc.edu)

* Fri Mar 02 2018 Trey Dockendorf <tdockendorf@osc.edu> 0.1.1-1
- Downgrade bc_osc_comsol to 0.1.1 (tdockendorf@osc.edu)

* Tue Feb 13 2018 Trey Dockendorf <tdockendorf@osc.edu> 0.2.0-1
- new package built with tito

