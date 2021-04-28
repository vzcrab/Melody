from ipa_parser import *

ipa_path = r'test/FlappyBird_v1.2.ipa'

ipa = IosIpa(ipa_path=ipa_path)
print_info(ipa)
print(ipa.infoplist_filepath)
# dump all icon apth
# print(ipa.get_icon_files())
