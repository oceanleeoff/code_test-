def solution(chicken):
    result = 0
    coupon_cnt = chicken

    while coupon_cnt >= 10 :
        new_chicken = coupon_cnt // 10
        result += new_chicken
        coupon_cnt = new_chicken + (coupon_cnt % 10)
          
    return result