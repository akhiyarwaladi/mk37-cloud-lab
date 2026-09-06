# PowerShell (Windows)
icacls.exe mk37-keypair-namaanda.pem /reset
icacls.exe mk37-keypair-namaanda.pem /grant:r "$($env:USERNAME):(R)"
icacls.exe mk37-keypair-namaanda.pem /inheritance:r
