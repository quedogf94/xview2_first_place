sudo apt update
sudo apt upgrade
snap install docker
sudo snap refresh snapd
snap install docker

git clone git@github.com:DIUx-xView/xView2_first_place.git
python inspect_images.py
python resize_images.py

#### AFter Resizing image 2 #####

docker run \
    -v $(pwd)/input:/input \
    -v $(pwd)/output:/output \
    ghcr.io/diux-xview/xview2_third_place/third_place:final \
    /input/1.png \
    /input/2_resized.png \
    /output/location.log \
    /output/class.log


python predict154_loc.py <pre_event_file_path> <post_event_file_path> <location_pred_file_path> <class_pred_file_path>
python predict154_loc.py input/1.png input/2_resized.png output/ output/



docker pull ghcr.io/diux-xview/xview2_fifth_place/baseline:final
docker run -it --rm ghcr.io/diux-xview/xview2_fifth_place/baseline:final --name xview2

