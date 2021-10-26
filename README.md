# lz4_decompress
A simple python script to decompress LZ4 DLLs.

Check out the below link for a full post explaining why this is necessary and under what circumstances it will be helpful. 
https://securitygrind.com/reverse-engineering-a-xamarin-application/

# Usage:
<code>./lz4_decompress input.dll</code>

This outputs a file in the form of <i>input_out.dll</i>, this assembly can now be decompiled using tools such as ILSpy. 
