package main

import (
	"errors"
	"flag"
	"fmt"
	"image"
	_ "image/jpeg"
	"image/png"
	"log"
	"os"
	"path/filepath"
	"strings"
)

var srcExt = flag.String("src", "jpg", "extention of input file")
var dstExt = flag.String("dst", "png", "extention of output file")

func convert(src string, dstExt string) error {
	file, err := os.Open(src)
	if err != nil {
		log.Fatalln("os open: ", err)
	}
	defer file.Close()

	srcImg, _, err := image.Decode(file)
	if err != nil {
		log.Fatalln("image decode: ", err)
	}
	dstImg := strings.Split(src, ".")[0] + "." + dstExt
	dst, err := os.Create(dstImg)
	defer dst.Close()
	switch dstExt {
	case "png":
		png.Encode(dst, srcImg)
	case "jpeg", "jpg":
		// jpeg.Encode(dst, srcImg)
	default:
		return errors.New("Not implemented: " + dstExt)
	}
	return nil
}

func main() {
	flag.Parse()
	args := flag.Args()

	if len(args) != 1 {
		fmt.Println("Usage: [option] <dirname>")
		os.Exit(1)
	}

	fmt.Println("[*] ", *srcExt, *dstExt, args[0])

	fileNames, err := filepath.Glob(filepath.Join(args[0], "*."+*srcExt))
	if err != nil {
		log.Fatalln("filepath Glob: ", err)
	}
	for _, src := range fileNames {
		if err := convert(src, *dstExt); err != nil {
			log.Fatalln("convert: ", err)
		}
	}
}
