# coding: UTF-8
import json
import time

DATASET = 'output'


def predict_add_flag_to_test_data_json(predict_file_name):
    # 把预测结果作为flag添加到test_data集
    with open('./' + DATASET + '/test_data.json', 'r', encoding='UTF-8') as test_data_json_file:
        test_data_json = json.load(test_data_json_file)
    with open('./' + DATASET + '/' + predict_file_name + '.txt', 'r', encoding='UTF-8') as predict_data_txt_file:
        for contents in test_data_json:
            for content_item in contents['Doc']['content']:
                predict_content_itm = predict_data_txt_file.readline()
                # 例如：两大股神跌落凡尘:没人能完全预测……'\t'[0.46323826909065247, 0.5367616415023804]'\n'
                # 先除去回车符以分隔符分隔，并且取第二项，还是数组，再取第二项，大于0.5则认为是观点句
                predict_content_itm = predict_content_itm.replace('\n', '')
                flag = predict_content_itm.split('\t')[1].split(',')[1].replace(']', '').replace(' ', '')
                if float(flag) >= 0.5:
                    content_item['flag'] = 1
                else:
                    content_item['flag'] = 0
    # 将预处理后的json存入文件
    with open('./' + DATASET + '/' + predict_file_name + '.json', 'w', encoding='utf-8') as pre_data_file:
        json.dump(test_data_json, pre_data_file, ensure_ascii=False, indent=4)
    print(predict_file_name + '.json' + "文件生成完毕")
    

def predict_json_to_label(predict_json_file_name):
    # 把预测json结果转换到test_label.json中
    with open('./' + DATASET + '/' + predict_json_file_name + '.json', 'r', encoding='UTF-8') as test_data_json_file:
        test_data_json = json.load(test_data_json_file)
    test_label_json = []
    for contents in test_data_json:
        for content_item in contents['Doc']['content']:
            if content_item['flag'] == 1:
                test_label_json_item = {
                    'event_id': contents['Descriptor']['event_id'],
                    'doc_id': contents['Doc']['doc_id'], 'start_sent_idx': content_item['sent_idx'],
                    'end_sent_idx': content_item['sent_idx']}
                test_label_json.append(test_label_json_item)
    # 将预处理后的json存入文件
    with open('./' + DATASET + '/' + predict_json_file_name + '_label' + '.json', 'w',
              encoding='utf-8') as pre_data_file:
        json.dump(test_label_json, pre_data_file, ensure_ascii=False, indent=4)
    print(predict_json_file_name + '_label' + '.json' + "文件生成完毕")


if __name__ == "__main__":
    # 把预测结果作为flag添加到test_data集
    predict_add_flag_to_test_data_json("predict_result")
    # 把预测json结果转换到test_label.json中
    predict_json_to_label("predict_result")

   