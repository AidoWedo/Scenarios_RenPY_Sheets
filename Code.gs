function doGet() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet();
  
  try {
    var scenes = getDataFromSheet(sheet.getSheetByName("Scenes"));
    var dialogue = getDataFromSheet(sheet.getSheetByName("Dialogue"));
    var choices = getDataFromSheet(sheet.getSheetByName("Choices"));
    var characters = getDataFromSheet(sheet.getSheetByName("Characters"));
    
    var data = {
      scenes: scenes,
      dialogue: dialogue,
      choices: choices,
      characters: characters
    };
    
    return ContentService.createTextOutput(JSON.stringify(data))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({error: error.message, stack: error.stack}))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

function getDataFromSheet(sheet) {
  if (!sheet) {
    throw new Error("Sheet not found. Please check if the sheet name is correct.");
  }
  
  var data = sheet.getDataRange().getValues();
  var headers = data.shift();
  return data.map(function(row) {
    var obj = {};
    headers.forEach(function(header, i) {
      obj[header] = row[i] === "" ? null : row[i];
    });
    return obj;
  });
}