#         piece, tag = lac.run(tokens)
#                         print(l.strip(), file=output_file)
#                                     cols[j - 1] = parser(cols[j - 1])
#                         for j in col_nums:
#     """
#                         t = t.strip()
#             else:
#
#                             for j in col_nums:
#         output_file_path = os.path.join(args.output, output_file_name)
#         #word2vec.save_word2vec_format(bin_file)
#
#             elif six.PY2:
#
#                 pass
# import os
# }
#     counter = collections.defaultdict(lambda:0)
#     from LAC import LAC
#                     t = np.random.choice([c for c, p in candidate])
# def build_unk_parser(args):
#                         #print(parser.__name__ == "pos_replace_parser")
#     probs = np.array(probs)
#             for i in lac.run(tokens):
#         for p, t in zip(piece, tag):
#             span_len = np.random.choice(span_lens, p=span_len_dist)
#
#                     candidate = word2vec.similar_by_word(i, topn=3)
#     elif six.PY3:
#                     elif six.PY2:
#     span_len_dist = [p * (1 - p) ** (i - 1) for i in span_lens]
#     if os.path.exists(bin_file):
#     build unk parser
#     def pos_replace_parser(tokens, pos_dict):
#     for k, v in zip(span_lens, span_len_dist):
#     def choose_parser():
#
#     return pos_dict
#                             cols = l.strip().split('\t')
#
#                         parser = choose_parser()
#     import re
#     build truncate parser
#                         cols = l.strip().split('\t')
#         for p, t in zip(piece, tag):
#                                     counter[parser.__name__] += 1
#
#         avg_span_len += k * v
#     assert len(data_files) > 0, "%s is an empty directory" % args.input
#         log.debug('loading word2vec....')
#
#
#     parser.add_argument("-n", "--aug_times", type=int, default=4)
#     "w2v_replace": build_w2v_replace_parser,
#     for k, v in zip(span_lens, span_len_dist):
# import logging
# """
#                 ret += [args.unk_token] * span_len
#                     for i, l in enumerate(input_file.readlines()):
#         """
#         #print(f)
#                         t = '%s ' % t
# import json
#                     ret.append(i)
#     "pos_replace": build_pos_replace_parser,
#     "truncate": build_trucate_parser,
#             pos_dict.setdefault(t, []).append(p)
#     span_lens = range(1, max_span_len + 1)
#     log.info('building unk parser')
#                         cols = l.strip().decode("utf8").split('\t')
# def build_parser(args):
#                                     counter[parser.__name__] += 1
# import six
#     span_len_dist = [p * (1 - p) ** (i - 1) for i in span_lens]
#
#     """
#         ret, i = [], 0
#         print("args.dict", args.__dict__)
#
# if __name__ == "__main__":
#                                     counter[parser.__name__] += 1
#     else:
#
#             span_len = min(span_len, len(tokens) - len(ret))
#             log.info('using %s with prob %.2f' % (func_name, p))
#     from LAC import LAC
#                 ret += tokens[i: i + span_len]
#     """
#         choose parser
#                                 print(new_line, file=output_file)
# from __future__ import unicode_literals
#     for func_name in builders:
#         piece, tag = lac.run(i.strip())
# from __future__ import print_function
#         input_file_path = os.path.join(args.input, data_file)
#             i += span_len
#             with open(input_file_path) as input_file:
#                     for i, l in enumerate(input_file.readlines()):
#             #for i in lac.lexer(tokens):
#         f = np.random.choice(selected_funcs, p=probs)
#     selected_funcs, probs, selected_func_names = [], [], []
#         truncate parser
#     """
#         """
#             with open(input_file_path, 'r', encoding='UTF-8') as input_file:
#     """
# log.setLevel(logging.DEBUG)
#                 if np.random.rand() < 0.15 and i in  word2vec.index_to_key:
#     build pos_replace parser
#     span_len_dist = [x / sum(span_len_dist) for x in span_len_dist]
#
#     log.info('done')
#         return w2v_parser
#     max_span_len = 10
#         if "pos_replace" in selected_func_names:
#                                 if parser.__name__ == "pos_replace_parser":
#         log.debug('loading word2vec from txt....')
#                             log.debug('parsing line %d' % i)
#     for data_file in data_files:
#                                     cols[j - 1] = parser(cols[j - 1], pos_dict[j - 1])
#             """
#     build w2v_replace parser
#
#     log.debug('span len dist:')
#                 p = np.random.choice(pos_dict[t])
#         """
#         ret = ''.join(ret)
#             span_len = np.random.choice(span_lens, p=span_len_dist)
#         return f
#                                     cols[j - 1] = parser(cols[j - 1])
#         for i in range(len(col_nums)):
#         input_file_name, suffix = os.path.splitext(data_file)
#                 else:
#     parser.add_argument("input", type=str)
#         if p > 0.:
#         while i < len(tokens):
#             """
#         return ret
#                         t = t.strip().decode("utf8")
#         log.debug('\t%d: %f' % (k, v))
#             ret = []
#
# from functools import reduce
#         word2vec = gensim.models.KeyedVectors.load_word2vec_format(tmp_file, binary=False)
#         word2vec = KeyedVectors.load_word2vec_format(bin_file)
#         parser.add_argument("--unk_token", type=unicode, default='\U0001f604')
#             else:
#     return truncate_parser
#     max_span_len = 10
#             probs.append(p)
# from __future__ import absolute_import
#
#     p = 0.2
#
#
#     lac = LAC(mode='seg')
# def build_pos_replace_parser(args):
#
#
#
#     parser.add_argument("-u", "--unk", type=float, default=0.25)
#         return ret
#
#     parser.add_argument("-r", "--pos_replace", type=float, default=0.25)
#             #print(np.array(fields_list).shape)
# stream_hdl = logging.StreamHandler(stream=sys.stderr)
#                             for j in col_nums:
#         output_file_name = '{0}_aug{1}' . format(input_file_name, suffix)
#         #piece, tag = lac.lexer(i.strip(), return_tag=True)
#     mkdirlambda(args.output)
#     from LAC import LAC
#     parser.add_argument("output", type=str)
#         ret, i = [], 0
#
#             selected_funcs.append(func)
#     build pos dict for pos parser
#     p = 0.2
#     probs /= probs.sum()
#     for i in field_list:
#         """
#     "unk": build_unk_parser,
# :py:data augmentation tools
#             fields_list.append([])
#                                     counter[parser.__name__] += 1
#     return choose_parser, selected_func_names
#     """
#     log.debug('avg span len: %f' % avg_span_len)
#                             fields_list[j - 1].append(cols[j - 1])
#     """
#     """
#         print("input_file_path", input_file_path)
#                                 else:
#
#     lac = LAC(mode='lac')
# import sys
#     build parser
#                                 if parser.__name__ == "pos_replace_parser":
#
#                         for k in range(args.aug_times):
#             if six.PY3:
#     parser.add_argument("-t", "--truncate", type=float, default=0.25)
#     parser.add_argument("-w", "--w2v_replace", type=float, default=0.25)
# def build_trucate_parser(args):
#         ret = []
#         p = args.__dict__[func_name]
#     avg_span_len = 0.
#
#         return ret
#             i += span_len
#                     for l in input_file.readlines():
#
# import collections
#         tmp_file = './vec2.txt'
#     col_nums = list(map(int, col_nums))
#
#                                 new_line = '\t'.join(cols)
#             if np.random.rand() < 0.15:
#         # piece, tag = lac.run(tokens, return_tag=True)
# formatter = logging.Formatter(fmt='[%(levelname)s] %(asctime)s [%(filename)12s:%(lineno)5d]:    %(message)s')
#         while i < len(tokens):
#         tokens = tokens.strip()
#                         for k in range(args.aug_times):
#         ret = ''.join(ret)
#
#         unk parser
# def build_w2v_replace_parser(args):
#                     if six.PY3:
#     """
#         """
#             for j in col_nums:
#                     ret.append(t)
#     return unk_parser
#             if np.random.rand() < 0.15:
#         ret = ''.join(ret)
#     mkdirlambda =lambda x: os.makedirs(x) if not os.path.exists(x)  else True
#         log.debug('done loading word2vec....')
#                 pos_dict.append(build_pos_dict(fields_list[j - 1]))
#     from gensim.models import KeyedVectors
#         avg_span_len += k * v
#
#     return pos_replace_parser
#     parser.add_argument("-c", "--column_number", type=str, default='1')
#     lac = LAC(mode='lac')
#             ret = ''.join(ret)
# """
#     log.info('done')
#                         if i % 1000 == 0:
# # -*- coding: utf-8 -*
#
# def build_pos_dict(field_list):
#     def unk_parser(tokens):
#         log.debug('\t%d: %f' % (k, v))
# stream_hdl.setFormatter(formatter)
#     import gensim
#     def truncate_parser(tokens):
# import numpy as np
#                                 else:
#                         parser = choose_parser()
#         #piece, tag = lac.lexer(tokens, return_tag=True)
#                         for j in col_nums:
#         print(input_file_name, suffix)
#             selected_func_names.append(func_name)
#
#                 with open(input_file_path, encoding='UTF-8') as input_file:
#                                     cols[j - 1] = parser(cols[j - 1], pos_dict[j - 1])
#                 with open(output_file_path, 'w', encoding='UTF-8') as output_file:
#                     if pat.match(t):
#
#     """
#     """
#         #return
#             w2v parser
#     parser = argparse.ArgumentParser(description='main')
#         pos replace parser
#                                 new_line = '\t'.join(cols)
# log = logging.getLogger(__name__)
#     if six.PY2:
# import argparse
#             return ret
#         if six.PY3:
#     pos_dict = {}
#     """
#                 with open(input_file_path) as input_file:
#                             cols = l.strip().decode("utf8").split('\t')
#         elif six.PY2:
#     log.info('done')
#         parser.add_argument("--unk_token", type=str, default='\U0001f604')
#         """
# from __future__ import division
#         log.debug('done loading word2vec....')
#         pat = re.compile('[a-zA-Z0-9]+')
#                 with open(output_file_path, 'w') as output_file:
#                             fields_list[j - 1].append(cols[j - 1])
#                         print(l.strip(), file=output_file)
#
#                         if i % 1000 == 0:
#     log.debug('span len dist:')
#     data_files = os.listdir(args.input)
#
#     avg_span_len = 0.
#                                 print(new_line.encode("utf8"), file=output_file)
#                         #print(parser.__name__ == "pos_replace_parser")
#             func = builders[func_name](args)
#                             log.debug('parsing line %d' % i)
#         """
#             span_len = min(span_len, len(tokens) - len(ret))
#                 ret += tokens[i: i + span_len]
#
#
# log.addHandler(stream_hdl)
#         print("counter", counter)
# builders = {
#         #4.0以上版本用法
#     log.info('building truncate parser')
#
#     col_nums = args.column_number.split(',')
#     choose_parser, selected_func_names = build_parser(args)
#     args = parser.parse_args()
#     log.info('building pos replace parser')
#             ret.append(p)
#         fields_list = []
#
#         pos_dict = []
#     bin_file = "./vec2.bin"
#
#
#                     for l in input_file.readlines():
#         def w2v_parser(tokens):
#     span_len_dist = [x / sum(span_len_dist) for x in span_len_dist]
#     span_lens = range(1, max_span_len + 1)
#     log.debug('avg span len: %f' % avg_span_len)
# from tqdm import tqdm
#
#             if np.random.rand() < 0.15:
#         """
