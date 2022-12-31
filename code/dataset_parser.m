FileData = load('Preprocessed_Database.mat');
data = FileData.Preprocessed_Database; 
cleanData = removevars(data,{'FilteredData'});
rawDataCol = [""];

for i = 1:40
    rawDataCol(i) = string(cleanData{i,1})+".csv";
    
end
cleanData.RawData = rawDataCol.';
writetable(cleanData,'myData.csv','Delimiter',',','QuoteStrings',true)

for i = 1:40
    rawData = data{i,2}{1,1};
    writetable(rawData,'filtererdData/'+rawDataCol(i),'Delimiter',',','QuoteStrings',true)
    disp("Done")
end
