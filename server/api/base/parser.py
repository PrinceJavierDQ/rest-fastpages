from rest_framework import parsers
from django.http import QueryDict


class NestedMultipartParser(parsers.MultiPartParser):
    """
    Parser for processing nested or array of nested field values as well as multipart files.
    Author: Prasit Gebsaap
    """

    def parse(self, stream, media_type=None, parser_context=None):
        result = super().parse(stream=stream, media_type=media_type, parser_context=parser_context)
        data = {}
        for key, value in result.data.items():
            if '[' in key and ']' in key:
                # print(key, ' and  ', value)
                keys = self.get_nested_keys(key)
                if len(keys) == 3:
                    nested_dict_key1 = keys[0]
                    nested_dict_key2 = keys[1]
                    nested_dict_key3 = keys[2]
                    if nested_dict_key2.isdigit():
                        #  array of data
                        index = int(nested_dict_key2)
                        if nested_dict_key1 not in data:
                            data[nested_dict_key1] = []
                            data[nested_dict_key1].append({nested_dict_key3: value})
                        elif index < len(data[nested_dict_key1]):
                            data[nested_dict_key1][index].update({nested_dict_key3: value})
                        else:
                            data[nested_dict_key1].append({nested_dict_key3: value})
                # TODO len(keys) == 2:
            else:
                data[key] = value
        print(data)

        # print(data)
        return parsers.DataAndFiles(data, result.files)

    def get_nested_keys(self, data):
        tmp_keys = data.split('[')
        keys = []
        for k in tmp_keys:
            keys.append(k.replace(']', ''))
        return keys
