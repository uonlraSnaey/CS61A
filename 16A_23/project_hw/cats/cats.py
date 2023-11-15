"""Typing test implementation"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    """select_value = [p for p in paragraphs if select(p)]
    return select_value[k]
    """
    count = -1
    for p in paragraphs:
        if select(p):
            count += 1
            if count == k:
                return p
    return ""
    # END PROBLEM 1

def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.


    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def select(paragraph):
        words = set(split(lower(remove_punctuation(paragraph))))
        for x in topic:
            if x in words:
              return True
        return False
    return select

    # END PROBLEM 2:



def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    """total_words = len(typed_words)
    correct_words = 0 
    
    if total_words == 0:
        return 0.0
    else:
        for tyred, refer in zip(typed_words, reference_words):
            flag = 0
            if typed_words == reference:
                flag = 1
            correctly_words += flag
            
        return 100*correct_words / total_words
     """
    total = len(typed_words)
    correct = 0
    if total == 0:
        return 0.0
    for t, r in zip(typed_words, reference_words):
        correct += (t == r)
    return  100*correct/total

    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    # END PROBLEM 4
    if typed == "":
        return 0.0
    else:
        '''typed_len = len(typed)
        word_typed = typed_len / 5
        time_ratio = 60 / elapsed
        '''
        return len(typed) * (12 / elapsed)

def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    if user_word in valid_words:
        return user_word
    else:
        words_diff = []
        for i in valid_words:
            diff = diff_function(user_word, i, limit)
            words_diff.append((i, diff))

        words_diff.sort(key=lambda item: item[1])
        if words_diff[0][1] <= limit:
            return words_diff[0][0]
        else:
            return user_word
        
        """
        else:
            words_diff = [(i, diff_function(user_word, i, limit)) for i in valid_words]
            min_diff_word = min(words_diff, key=lambda item: item[1])

            if min_diff_word[1] <= limit:
                return min_diff_word[0]
        """

    
    # END PROBLEM 5


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    # 知道怎么做但是没考虑循环怎么办？
    # 多半是装的 <3
    if len(start) == 0:
        return len(goal)
    if len(goal) == 0:
        return len(start)
    if start[0] != goal[0]:
        if limit == 0:
            return 1
        else:
            return 1 + shifty_shifts(start[1:], goal[1:], limit-1)
    else:
        return shifty_shifts(start[1:], goal[1:], limit)
   # END PROBLEM 6


def meowstake_matches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""

    if limit < 0: # Fill in the condition
        # BEGIN
        "*** YOUR CODE HERE ***"
        return 0
        # END

    elif len(start) == 0 or len(goal) == 0: # Feel free to remove or add additional cases
        # BEGIN
        "*** YOUR CODE HERE ***"
        #return 0
        return len(start) + len(goal)
        # END
    elif start[0] == goal[0]:
        return meowstake_matches(start[1:], goal[1:], limit)
    else:
        add_diff = meowstake_matches(start, goal[1:], limit-1) # Fill in these lines
        remove_diff = meowstake_matches(start[1:], goal, limit-1)
        substitute_diff = meowstake_matches(start[1:], goal[1:], limit-1)
        # BEGING
        "*** YOUR CODE HERE ***"
        return 1 + min(add_diff, remove_diff, substitute_diff)
        # END


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    """
    len_t, len_p = len(typed), len(prompt)
    assert len_t > len_p, 'typed is shorter than prompt'
    count = 0 
    for l in len_p:
        if typed[i] != prompt[i]:
            break
        count += 1
    correct_ratio = count / len_p
    
    send({'id': id, 'progress': correct_ratio})
    return correct_ratio
    """
    """
    什么时候我才能写出这样漂亮的代码qwq
    """

    correct_sofar = 0
    for t, p in zip(typed, prompt):
        if t == p:
            correct_sofar += 1
        else:
            break
    progress = correct_sofar / len(prompt)
    send({'id': id, 'progress': progress})
    return progress
        

    # END PROBLEM 8

def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    time_spend = []

    for player in times_per_player: # 统计词数
        time = []
        for i in range(len(player) - 1):
            time.append(player[i+1] - player[i])
        time_spend.append(time)
    return game(words, time_spend)
    # END PROBLEM 9
    


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    players = range(len(all_times(game)))  # An index for each player
    words = range(len(all_words(game)))    # An index for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    """
    # words, times = game
    words = all_words(game)
    times = all_words(game)
    fastest_w = [[] for _ in range(len(times))]
    # 捏马马的不会了
    for index, word in enumerate(words):
        word_times = [times(player)[index] for player in range(len(times))]
        word_index = min(range(len(times)), key=lambda x: word_times[x])
        fastest_w[word_index].append(word)

    return fastest_w

    很烦WAW nmd cnm 把 338 行删了一行 还tm测半天
    """
    words = all_words(game)
    times = all_times(game)
    tot_player = len(times) 
    fastest = [[] for i in range(tot_player)]
    for i, word in enumerate(words):
        word_times = [times[player][i] for player in range(tot_player)]
        idx = min(range(tot_player), key=lambda x: word_times[x])
        fastest[idx].append(word)
    return fastest

    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]

def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you

##########################
# Extra Credit #
##########################

key_distance = get_key_distances()
def key_distance_diff(start, goal, limit):
    """ A diff function that takes into account the distances between keys when
    computing the difference score."""

    start = start.lower() #converts the string to lowercase
    goal = goal.lower() #converts the string to lowercase

    # BEGIN PROBLEM EC1
    "*** YOUR CODE HERE ***"
    """ 和 meowstake_matches 相似  区别是差值换成了键盘上字母的距离"""
    if limit < 0:
        return float("inf")
    if len(goal) == 0 or len(start) == 0:
        return len(goal) + len(start)
    elif start[0] == goal[0]:
        return key_distance_diff(start[1:], goal[1:], limit)
    else:
        add_diff = 1 + key_distance_diff(start, goal[1:], limit - 1) # 向 start 添加 比 goal 少的字母
        del_diff = 1 + key_distance_diff(start[1:], goal, limit - 1)# 从 start 中删除 goal 中没有的字母
        # start 和 goal 中对应的字母不相等
        distance = key_distance[(start[0], goal[0])]
        disorder_diff = distance + key_distance_diff(start[1:], goal[1:], limit - 1)

        return min(min(add_diff, del_diff), disorder_diff)
    # END PROBLEM EC1

def memo(f):
    """A memoization function as seen in John Denero's lecture on Growth"""

    cache = {}
    def memoized(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return memoized



def faster_autocorrect(user_word, valid_words, diff_function, limit):
    """A memoized version of the autocorrect function implemented above."""

    # BEGIN PROBLEM EC2
    "*** YOUR CODE HERE ***"
    """ OK 完全不会， 开摆！"""

    index = tuple([user_word, tuple(valid_words), diff_function, limit])
    if user_word in valid_words:
        return user_word
    if index in memo_for_far:
        return memo_for_far[index]
    else:
        words_diff = [diff_function(user_word, w, limit) for w in valid_words]
        similar_word, similar_diff = min(zip(valid_words, words_diff), key=lambda item: item[1])
        if similar_diff > limit:
            ret = user_word
        else:
            ret = similar_word
        memo_for_far[index] = ret
        return ret
    # END PROBLEM EC2


##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
