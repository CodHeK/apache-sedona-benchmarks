import subprocess, sys, time

def pre_process_data(name):
    file = name + '.wkt'
    tmp_file = name + '_tmp.wkt'

    cmd1 = 'awk -F"|" -v OFS="\t" \' $1=$1 \' ./sedona_osm_data/' + file + ' > ./sedona_osm_data/' + tmp_file

    subprocess.call(cmd1, shell=True)

    cmd2 = 'awk \'{gsub(/"/," ")}1\' ./sedona_osm_data/' + tmp_file + ' > ./sedona_osm_data/' + file

    subprocess.call(cmd2, shell=True)

    cmd3 = 'rm ./sedona_osm_data/' + tmp_file

    subprocess.call(cmd3, shell=True)


files = ['all_points_1K', 'all_points_10K', 'all_points_100K', 'all_source_1K', 'all_source_10K', 'all_source_100K']

for file in files:
    pre_process_data(file)
    print(file + " done!")
    time.sleep(0.5)