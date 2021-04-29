package main

import (
	"encoding/json"
	"fmt"
	"github.com/phinexdaz/ipapk"
	"image"
	"image/gif"
	"image/jpeg"
	"image/png"
	"log"
	"os"
	"path"
	"path/filepath"
	"strconv"
	"strings"
)

// 判断文件夹是否存在
func PathExists(path string) (bool, error) {
	_, err := os.Stat(path)
	if err == nil {
		return true, nil
	}
	if os.IsNotExist(err) {
		return false, nil
	}
	return false, err
}

func SaveImage(p string, src image.Image) error {
	sDir := path.Dir(p)
	exist, err := PathExists(sDir)
	if !exist {
		os.Mkdir(sDir, os.ModePerm)
	}
	f, err := os.OpenFile(p, os.O_SYNC|os.O_RDWR|os.O_CREATE, 0666)
	if err != nil {
		return err
	}
	defer f.Close()
	ext := filepath.Ext(p)
	if strings.EqualFold(ext, ".jpg") || strings.EqualFold(ext, ".jpeg") {
		err = jpeg.Encode(f, src, &jpeg.Options{Quality: 80})
	} else if strings.EqualFold(ext, ".png") {
		err = png.Encode(f, src)
	} else if strings.EqualFold(ext, ".gif") {
		err = gif.Encode(f, src, &gif.Options{NumColors: 256})
	}
	return err
}

type App struct {
	Name       string
	BundleID   string
	Version    string
	SdkVersion string
	Size       string
	Icon       string
}

func Parser(path string) {

	files := path
	apk, _ := ipapk.NewAppParser(files)
	appParser := &App{}
	appParser.Name = apk.Name
	appParser.BundleID = apk.BundleId
	appParser.Version = apk.Version
	appParser.SdkVersion = apk.Build
	appParser.Size = strconv.FormatInt(apk.Size, 10)
	if apk.Icon != nil {
		dir, err := os.Getwd()
		if err != nil {
			log.Fatal(err)
		}
		SaveImage(dir+"/"+apk.BundleId+"/icon.png", apk.Icon)
		appParser.Icon = apk.BundleId + "/icon.png"
	} else {
		appParser.Icon = "None"
	}
	data, _ := json.Marshal(appParser)
	fmt.Println(string(data))
}
func main() {
	argNum := len(os.Args[1:])
	if argNum < 1 {
		println("args no enough!")
	} else {
		var path = os.Args[1]
		Parser(path)
	}

}
