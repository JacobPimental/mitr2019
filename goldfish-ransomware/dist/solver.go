package main
import "os"
import "crypto/cipher"
import "crypto/des"
//import "encoding/hex"
import b64 "encoding/base64"
import "fmt"
//import    "bufio"
//import    "io"
import    "io/ioutil"


func main() {
	b64key := os.Args[1] //"Nzqx6P1QxUry+a1qMq0cBtiFJonC3PPB"
	key,_  := b64.StdEncoding.DecodeString(b64key)
	d,_  := ioutil.ReadFile("important-file.png.enc")
	ciphertext, _ := b64.URLEncoding.DecodeString(string(d))
	block, err := des.NewTripleDESCipher(key)
	if err != nil {
		panic(err)
	}
	iv := ciphertext[:8]
	ciphertext = ciphertext[8:]
	//fmt.Printf("%s", iv)
	stream := cipher.NewCFBDecrypter(block, iv)
	stream.XORKeyStream(ciphertext, ciphertext)
	fmt.Printf("%s", ciphertext)
}
