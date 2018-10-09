# 袋の種類
BAG_A = 0
BAG_B = 1

# 玉の色
BALL_RED = 0
BALL_WHITE = 1

# 袋を選ぶ確率
_prob_bag = []
_prob_bag.insert(BAG_A, 1/2)
_prob_bag.insert(BAG_B, 1/2)

# 袋内の玉の色を選ぶ確率
_prob_ball = []

_prob_ball_a = []
_prob_ball_a.insert(BALL_RED, 2/3)
_prob_ball_a.insert(BALL_WHITE, 1/3)
_prob_ball.insert(BAG_A, _prob_ball_a)

_prob_ball_b = []
_prob_ball_b.insert(BALL_RED, 1/4)
_prob_ball_b.insert(BALL_WHITE, 3/4)
_prob_ball.insert(BAG_B, _prob_ball_b)

# 事後確率を計算する
def posterior(ball_list, bag):
    if len(ball_list) == 1:
        return _prob_ball[bag][ball_list[0]] * _prob_bag[bag]
    else:
        return _prob_ball[bag][ball_list[0]] * posterior(ball_list[1:], bag)

# 袋Aが選ばれる確率を計算する
def posterior_a(ball_list):
    return posterior(ball_list, BAG_A) / (posterior(ball_list, BAG_A) + posterior(ball_list, BAG_B))

ball = [BALL_RED] * 5 * 5
ball.extend([BALL_WHITE] * 3 * 5)
print(posterior_a(ball))
