def solution(id_pw, db):
    result = []
    user_id, user_pw = id_pw[0], id_pw[1]
    
    for i in range(len(db)) :
        if db[i][0] != user_id :
            result.append('fail')
        elif db[i][1] != user_pw :
            result.append('wrong pw')
        else :
            result.append('login')
    
    if 'login' in result :
        return 'login'
    elif 'wrong pw' in result :
        return 'wrong pw'
    else :
        return 'fail'
        