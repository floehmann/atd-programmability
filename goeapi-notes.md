### `go` notes

###### as arista shell 1
```
sudo -i
cd /usr/local
curl -O https://dl.google.com/go/go1.12.9.linux-amd64.tar.gz
tar xvfz go1.12.9.linux-amd64.tar.gz 
```

###### as arista shell 2
```
export PATH=$PATH:/usr/local/go/bin

mkdir -p $HOME/go/src

mkdir  $HOME/go/src/hello
```
```
cd $HOME/go/src/hello

cat > ./hello.go <<EOF
package main

import "fmt"

func main() {
	fmt.Printf("hello, world\n")
}
EOF
```

```
go build
```

```
./hello
```

### check out `goeapi`

https://github.com/aristanetworks/goeapi


###### as arista

```
go get github.com/aristanetworks/goeapi
cd /home/arista/go/src/github.com/aristanetworks/goeapi
make bootstrap
```

```
cd
cat > ~/.eapi.conf <<EOF
[connection:leaf1]
host=192.168.0.14
username=arista
password=arista
enablepwd=passwd
transport=https
EOF
```

```
mkdir /home/arista/go/src/goeapi-example1
cd /home/arista/go/src/goeapi-example1
```

```
cat > example1.go <<EOF
package main

import (
	"fmt"

	"github.com/aristanetworks/goeapi"
	"github.com/aristanetworks/goeapi/module"
)

func main() {
	node, err := goeapi.ConnectTo("leaf1")
	if err != nil {
		panic(err)
	}
	conf := node.RunningConfig()
	fmt.Println(conf)

	var showversion module.ShowVersion
	handle, _ := node.GetHandle("json")
	if err := handle.Enable(&showversion); err != nil {
		panic(err)
	}

	fmt.Println("\nVersion:", showversion.Version)

	s := module.Show(node)
	showData := s.ShowVersion()
	fmt.Printf("\nModelname         : %s\n", showData.ModelName)
	fmt.Printf("Internal Version  : %s\n", showData.InternalVersion)
	fmt.Printf("System MAC        : %s\n", showData.SystemMacAddress)
	fmt.Printf("Serial Number     : %s\n", showData.SerialNumber)
	fmt.Printf("Mem Total         : %d\n", showData.MemTotal)
	fmt.Printf("Bootup Timestamp  : %.2f\n", showData.BootupTimestamp)
	fmt.Printf("Mem Free          : %d\n", showData.MemFree)
	fmt.Printf("Version           : %s\n", showData.Version)
	fmt.Printf("Architecture      : %s\n", showData.Architecture)
	fmt.Printf("Internal Build ID : %s\n", showData.InternalBuildID)
	fmt.Printf("Hardware Revision : %s\n", showData.HardwareRevision)

	sys := module.System(node)
	if ok := sys.SetHostname("Ladie"); !ok {
		fmt.Printf("SetHostname Failed\n")
	}
	sysInfo := sys.Get()
	fmt.Printf("\nSysinfo: %#v\n", sysInfo.HostName())
}
EOF
```

```
go build
```

```
./goeapi-example1
```
