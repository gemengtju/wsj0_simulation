#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Ge Meng

import os

WSJ0_DATA_DIR="/Work18/2015/gemeng/data/raw_wsj0_data/"
WSJ0_MC_DATA_DIR="/CDShare/wsj0-mix-mc/"
TARGET_DIR="./wsj0_mix_mc_extr/"

def create_speaker_extraction_data():
    print("start...")
    for data_type in ['cv', 'tt','tr']:
        list_path = "./mix_2_spk_" + data_type + "_extr.txt"
        lists = open(list_path).readlines()
        for item in lists:
            tokens = item.strip().split()
            (_, s1_name) = os.path.split(tokens[0])
            (s1_uttid, _) = os.path.splitext(s1_name)
            (_, s2_name) = os.path.split(tokens[2])
            (s2_uttid, _) = os.path.splitext(s2_name)
            (_, aux_name) = os.path.split(tokens[4])
            (aux_uttid, _) = os.path.splitext(aux_name)
            mix_name = s1_uttid + '_' + tokens[1] + '_' + s2_uttid + '_' + tokens[3] + '.wav'
            speaker_extraction_mix_name = s1_uttid + '_' + tokens[1] + '_' + s2_uttid + '_' + tokens[3] + '_' + aux_uttid + '.wav'
            mix_path = os.path.join(WSJ0_MC_DATA_DIR, '2speakers_reverb', 'wav8k', 'max', data_type, 'mix', mix_name)
            s1_path = os.path.join(WSJ0_MC_DATA_DIR, '2speakers_reverb', 'wav8k', 'max', data_type, 's1', mix_name)
            aux_path = os.path.join(WSJ0_DATA_DIR, tokens[4].replace('.wv1', '.wav'))
            if not os.path.exists(os.path.join(TARGET_DIR, data_type)):
                #os.makedirs(os.path.join(TARGET_DIR, data_type, 'mix'))
                #os.makedirs(os.path.join(TARGET_DIR, data_type, 's1'))
                os.makedirs(os.path.join(TARGET_DIR, data_type, 'aux'))
            #os.system("cp " + mix_path + " " + os.path.join(TARGET_DIR, data_type, 'mix', speaker_extraction_mix_name))
            #os.system("cp " + s1_path + " " + os.path.join(TARGET_DIR, data_type, 's1', speaker_extraction_mix_name))
            os.system("cp " + aux_path + " " + os.path.join(TARGET_DIR, data_type, 'aux', speaker_extraction_mix_name))

        #mix_name, target_name, aux_name = load_txt(data_type)
        ## move file /CDShare/wsj0-mix-mc/2speakers_anechoic/wav8k/max/tt
        ## /Work18/2015/gemeng/project/ss/speaker_extraction/data/wsj0_2mix_extr/wav8k/max/tr/
        #mix_path = os.path.join(WSJ_DATA_DIR, '2speakers_reverb', 'wav8k', 'max', data_type, 'mix', mix_name)
        #s1_path = os.path.join(WSJ_DATA_DIR, '2speakers_anechoic', 'wav8k', 'max', data_type, 's1', target_name)
        #aux_path = os.path.join(WSJ_DATA_DIR, '2speakers', 'wav8k', 'max', data_type, 'aux', aux_name)
        #save_path = os.path.join(TARGET_DIR, '2speakers_extr', 'wav8k', 'max', data_type)
        ## mkd_target_dir
        #os.system('cp ' + mix_path + ' ' + save_path + ' ' + )


if __name__ == "__main__":
    create_speaker_extraction_data()
