import requests as req
url='https://restful-booker.herokuapp.com'

def describe_booking(booking_id):
    res="{0}/booking/{1}".format(url, booking_id)
    print(res)
    return req.get(res)

if __name__=='__main__':
    res=describe_booking(2)
    print("\nStatus code: {0}. \nText: {1}".format(res,res.text ))
