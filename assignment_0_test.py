# %%
import MLMech_kickoff.assignment_0 as assignment_0

def test_sum():
    assert assignment_0.get_sum(1, 2) == 3

def test_difference():
    assert assignment_0.get_difference(3, 2) == 1

def test_product():
    assert assignment_0.get_product(2, 3) == 6

def test_float_quotient():
    assert assignment_0.get_float_quotient(1, 2) == 0.5

def test_floored_quotient():
    assert assignment_0.get_floored_quotient(3, 2) == 1

def test_remainder():
    assert assignment_0.get_remainder(3, 2) == 1

def test_power():
    assert assignment_0.get_power(3, 2) == 9

def test_path():
    assert assignment_0.get_path('test') == r'C:\users\newbie\Documents\test'

def test_get_rid_of_whitespace():
    assert assignment_0.get_rid_of_whitespace('   \ttest 123\n   ') == 'test 123'
    assert assignment_0.get_rid_of_whitespace(r'   \ttest 123\n   ') == r'\ttest 123\n'

def test_get_rid_of_leading_whitespace():
    assert assignment_0.get_rid_of_leading_whitespace('  \n123!test \t  ') == '123!test \t  '
    assert assignment_0.get_rid_of_leading_whitespace(r'  \n123!test \t  ') == r'\n123!test \t  '

def test_get_rid_of_trailing_whitespace():
    assert assignment_0.get_rid_of_trailing_whitespace('  \ttest123!  \n') == '  \ttest123!'
    assert assignment_0.get_rid_of_trailing_whitespace(r'  \ttest123!  \n') == r'  \ttest123!  \n'

def test_get_nth_letter_second():
    assert assignment_0.get_nth_letter_second('supercalifragilisticexpialidocious', 2, 3-1) == 'prairglsiepaioiu'
    assert assignment_0.get_nth_letter_second('supercalifragilisticexpialidocious', 5, 2-1) == 'uaasxio'

def test_get_last_n_letters():
    assert assignment_0.get_last_n_letters('supercalifragilisticexpialidocious', 5) == 'cious'

def test_replace_first_letter():
    assert assignment_0.get_first_letter_changed('joker', 'p') == 'poker'
    assert assignment_0.get_first_letter_changed('coincidence', 'j') == 'joincidence'

def test_get_length_of_string():
    assert assignment_0.get_length_of_string('supercalifragilisticexpialidocious') == 34
    assert assignment_0.get_length_of_string('test123') == 7

def test_get_string_as_list():
    assert assignment_0.get_string_as_list('supercalifragilisticexpialidocious') == ['s', 'u', 'p', 'e', 'r', 'c', 'a', 'l', 'i', 'f', 'r', 'a', 'g', 'i', 'l', 'i', 's', 't', 'i', 'c', 'e', 'x', 'p', 'i', 'a', 'l', 'i', 'd', 'o', 'c', 'i', 'o', 'u', 's']
    assert assignment_0.get_string_as_list('test123') == ['t', 'e', 's', 't', '1', '2', '3']

def test_get_first_part_after_split():
    assert assignment_0.get_first_part_after_split('supercalifragilisticexpialidocious', 'p') == 'su'
    assert assignment_0.get_first_part_after_split('test123', 'a') == 'test123'
    assert assignment_0.get_first_part_after_split('test123', 't') == ''

def test_get_last_two_parts_concatenated_after_split():
    assert assignment_0.get_last_two_parts_concatenated_after_split('Helene', 'e') == 'n'

def test_get_list_with_appended_element():
    assert assignment_0.get_list_with_appended_element(list('tes'), 't') == ['t', 'e', 's', 't']

def test_get_length_of_list():
    assert assignment_0.get_length_of_list(['t', 'e', 's', 't', '1', '2', '3']) == 7
    assert assignment_0.get_length_of_list(['s', 'u', 'p', 'e', 'r', 'c', 'a', 'l', 'i', 'f', 'r', 'a', 'g', 'i', 'l', 'i', 's', 't', 'i', 'c', 'e', 'x', 'p', 'i', 'a', 'l', 'i', 'd', 'o', 'c', 'i', 'o', 'u', 's']) == 34