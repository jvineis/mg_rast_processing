# mg_rast_processing
Sick of struggling with the MG-RAST website and can't get the API to do what you are asking.  Here is a step by step process to pull the data that you want from MG-RAST
Here are the steps to generate tables for the desired data from MGRAST.
1.  Run; bash to_get_functinoal_url.shx - A VERY IMPORTANT POINT - you need to make sure that you have your own access key from MGRAST website which you can retrieve from here:
http://www.mg-rast.org/mgmain.html?mgpage=upload by clicking the webkey link. 
this script produces a collection of urls to whatever you requested (taxonomy or function at different levels of stringency etc.)
The output should look like this
{"url":"http://api.metagenomics.anl.gov/status/4a38356c-4bfc-4d85-8cbb-de5b0274b36c","id":"4a38356c-4bfc-4d85-8cbb-de5b0274b36c","status":"submitted"}
and the url address is whats important here.  

Your request may take some time to complete, you will know when it is done by the amount of output produced by running the command below which requests table from MGRAST
curl http://api.metagenomics.anl.gov/status/4a38356c-4bfc-4d85-8cbb-de5b0274b36c

If it spits out a lot of text followed by strings of numbers, you know its done.  and you are ready to write that table to an output like this
curl http://api.metagenomics.anl.gov/status/4a38356c-4bfc-4d85-8cbb-de5b0274b36c > my_table.biom

Then you can convert this taxonomy biom file into a matrix like below.
python speciesbiomtotxt.py my_table.biom my_table.txt

or functinoal biom file into into a matrix like below.
python biomtotxt.py my_table.biom my_table.txt


