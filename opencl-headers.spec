%global cl_headers_commit e55138572c81dce15ffe402bd1142d9652ec5cb5
%global date 20260317
%global cl_headers_shortcommit %(c=%{cl_headers_commit}; echo $c | cut -c1-7)
%global cl_hpp_commit 40b6833d8c08de691c00e49bfca7081b06f53dd4
%global cl_hpp_shortcommit %(c=%{cl_hpp_commit}; echo $c | cut -c1-7)

Name:           opencl-headers
Version:        3.0
Release:        1.qli%{?cl_headers_shortcommit:.%{date}git%{cl_headers_shortcommit}}%{?dist}
Summary:        OpenCL (Open Computing Language) header files

License:        Apache-2.0
URL:            https://www.khronos.org/registry/cl/

Source0:        https://github.com/KhronosGroup/OpenCL-Headers/archive/%{cl_headers_commit}/OpenCL-Headers-%{cl_headers_shortcommit}.tar.gz
Source1:        https://github.com/KhronosGroup/OpenCL-CLHPP/archive/%{cl_hpp_commit}/OpenCL-CLHPP-%{cl_hpp_shortcommit}.tar.gz

BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup -n OpenCL-Headers-%{cl_headers_commit}

tar -xf %{SOURCE1}
cp -p OpenCL-CLHPP-%{cl_hpp_commit}/include/CL/{cl2,opencl}.hpp .

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_includedir}/CL/
install -p -m 0644 *hpp CL/* -t %{buildroot}%{_includedir}/CL/
# We're not interested in Direct3D things
rm -vf %{buildroot}%{_includedir}/CL/cl_{dx9,d3d}*
# Install pkgconfig files
mkdir -p %{buildroot}%{_datadir}/pkgconfig
sed -e 's|@CMAKE_INSTALL_PREFIX@|%{_prefix}|' -e 's|@OPENCL_INCLUDEDIR_PC@|%{_includedir}|' OpenCL-Headers.pc.in > %{buildroot}%{_datadir}/pkgconfig/OpenCL-Headers.pc
sed -e 's|@CMAKE_INSTALL_PREFIX@|%{_prefix}|' -e 's|@OPENCLHPP_INCLUDEDIR_PC@|%{_includedir}|' OpenCL-CLHPP-%{cl_hpp_commit}/OpenCL-CLHPP.pc.in > %{buildroot}%{_datadir}/pkgconfig/OpenCL-CLHPP.pc

%files
%dir %{_includedir}/CL
%{_includedir}/CL/cl2.hpp
%{_includedir}/CL/cl_egl.h
%{_includedir}/CL/cl_ext.h
%{_includedir}/CL/cl_ext_intel.h
%{_includedir}/CL/cl_function_types.h
%{_includedir}/CL/cl_gl_ext.h
%{_includedir}/CL/cl_gl.h
%{_includedir}/CL/cl.h
%{_includedir}/CL/cl_half.h
%{_includedir}/CL/cl_icd.h
%{_includedir}/CL/cl_layer.h
%{_includedir}/CL/cl_platform.h
%{_includedir}/CL/cl_va_api_media_sharing_intel.h
%{_includedir}/CL/cl_version.h
%{_includedir}/CL/opencl.h
%{_includedir}/CL/opencl.hpp
%{_datadir}/pkgconfig/OpenCL-Headers.pc
%{_datadir}/pkgconfig/OpenCL-CLHPP.pc

%changelog
* Wed Sep 30 2026 Maintainers.pkg-rpm-opencl-headers <Maintainers.pkg-rpm-opencl-headers@qualcomm.com> - 3.0-1.qli.20260317gite551385
- Imported from https://gitlab.com/redhat/centos-stream/rpms/opencl-headers.git
- Update OpenCL-Headers to e55138572c81dce15ffe402bd1142d9652ec5cb5
- Update OpenCL-CLHPP to 40b6833d8c08de691c00e49bfca7081b06f53dd4

