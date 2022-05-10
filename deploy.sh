python3 main.py -c
rm -rf output.docker/*
mkdir deploy/
mv dist/* deploy/
cp -ru src/* deploy/
mkdir output.docker
podman run --rm -e LANG=C.UTF-8 -e LC_ALL=C.UTF-8 --tmpfs /tmp -v ./:/data sridca/emanote emanote -L "/data/deploy" gen /data/output.docker
rm -rf deploy/
