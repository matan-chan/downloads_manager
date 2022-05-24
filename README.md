# downloads manager
Who among us hasn't had downloads folder full of unordered files and junk?
**downloads manager** will sort all of your files in the download's folder in an easy and efficient manner.
To config which file type will go where and where the download folder is open the `config.json` file and
add or change lines you can also config how many times the script will run through the downloads' folder.
here's the config file.
```json
{
  "downloads_folder": "C:/Users/Snir/Desktop",
  "loop_every_x_second": 300,
  "types": [
    {
      "type": ".mp3",
      "path": "C:/Users/Snir/Desktop/songs"
    },
    {
      "type": ".pdf",
      "path": "C:/Users/Snir/Desktop/pdfs"
    }
  ]
}
```

Lets say i want all the mp4 files to go to my mp4_files_folder folder on my desktop.

```json
{
  "downloads_folder": "C:/Users/Snir/Desktop",
  "loop_every_x_second": 300,
  "types": [
    {
      "type": ".mp3",
      "path": "C:/Users/Snir/Desktop/songs"
    },
    {
      "type": ".pdf",
      "path": "C:/Users/Snir/Desktop/pdfs"
    }
    {
      "type": ".mp4",
      "path": "C:/Users/Snir/Desktop/mp4_files_folder"
    }
  ]
}
```

