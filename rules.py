def grouprules(groupid,getmsg,msg,sendmsg,port):
    import requests
    
    if getmsg == msg:                       #if 消息 == 6：
        requests.get("http://127.0.0.1:"+port+"/send_group_msg?group_id="+groupid+"&message="+sendmsg)

def privaterules(priid,getmsg,msg,sendmsg,port):
    import requests
    
    if getmsg == msg:                       #if 消息 == 6：
        requests.get("http://127.0.0.1:"+port+"/send_private_msg?user_id="+priid+"&message="+sendmsg)