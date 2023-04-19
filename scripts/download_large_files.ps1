# Read Google Drive file ID from the config file
$FileID = Get-Content -Path "google_drive_file_id.config"

# Construct the URL using the file ID
$URL = "https://drive.google.com/uc?export=download&id=$FileID"

$FILENAME = "large_files.zip"
$DESTINATION = "$PSScriptRoot\..\large_files"

# Create destination directory if it doesn't exist
if (!(Test-Path -Path $DESTINATION)) {
    New-Item -ItemType Directory -Path $DESTINATION | Out-Null
}

# Download the file
Write-Host "Downloading $FILENAME..."
Invoke-WebRequest -Uri $URL -OutFile $FILENAME

# Extract the file using Expand-Archive cmdlet (assuming you have a .zip file)
Write-Host "Extracting $FILENAME..."
Expand-Archive -Path $FILENAME -DestinationPath $DESTINATION

# Remove the downloaded file after extraction
Remove-Item $FILENAME

Write-Host "Download and extraction completed."