class FlatIterator:

    def __init__(self, list_of_list):

        def __reqursiya(s):
            if s == []:
                return s
            if isinstance(s[0], list):
                return(__reqursiya(s[0]) + __reqursiya(s[1:]))
            return(s[:1] + __reqursiya(s[1:]))

        self.index = 0
        self.new_list = __reqursiya(list_of_list)
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.new_list):
            raise StopIteration
        items = self.new_list[self.index]
        self.index += 1
        return items


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    object = FlatIterator(list_of_lists_2)
    print(type(object))

    # for i in object:
    #     print(i)

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()