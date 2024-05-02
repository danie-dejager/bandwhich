Name:           bandwhich
Version:        0.22.2
Release:        3%{?dist}
Summary:        Terminal bandwidth utilization tool

License:        MIT
URL:            https://github.com/imsnif/bandwhich
Source0:        https://github.com/imsnif/bandwhich/archive/refs/tags/v%{version}.tar.gz

%description
Terminal bandwidth utilization tool

%global debug_package %{nil}

%prep
%setup -q

%build
# Install Rust using curl
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
export PATH="$PATH:$HOME/.cargo/bin"
cargo build --release
strip --strip-all target/release/%{name}

%install
mkdir -p %{buildroot}/%{_bindir}
upx target/release/%{name}
install -m 755 target/release/%{name} %{buildroot}/%{_bindir}/%{name}

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
