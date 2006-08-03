#
# Rebuild option:
#
#   --with testsuite         - run the test suite
#

Name:           perl-GSSAPI
Version:        0.23
Release:        1%{?dist}
Summary:        Perl extension providing access to the GSSAPIv2 library

Group:          Development/Libraries
License:        GPL or Artistic
URL:            http://search.cpan.org/dist/GSSAPI/
Source0:        http://www.cpan.org/authors/id/A/AG/AGROLMS/GSSAPI-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  perl
BuildRequires:  krb5-devel
BuildRequires:  which
BuildRequires:  perl(Test::Pod) >= 1.00
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module gives access to the routines of the GSSAPI library, as
described in rfc2743 and rfc2744 and implemented by the Kerberos-1.2
distribution from MIT.


%prep
%setup -q -n GSSAPI-%{version}
chmod a-x examples/*.pl


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
# fails a couple of tests if network not available
%{?_with_testsuite:make test}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes README examples/
%{perl_vendorarch}/GSSAPI*
%{perl_vendorarch}/auto/GSSAPI/
%{_mandir}/man3/*.3*


%changelog
* Thu Aug  3 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.23-1
- Update to 0.23.

* Mon May 29 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.22-1
- Update to 0.22.

* Thu Apr  6 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.21-1
- Update to 0.21.

* Fri Mar 31 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.20-1
- First build.
