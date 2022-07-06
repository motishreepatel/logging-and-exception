import logging
logging.basicConfig(filename = "ext_list.log", level = logging.DEBUG)

class Get_all_lists:

    def extract_lists_in_given_list(self,l):
        """extract all the lists available in given list
        :param l: input list
        :return:returning a list containing all the lists in given list"""

        try:
            l3=[]
            logging.info("the given list is %s", l)
            for i in l :
                if (type(i) == list) :
                    l3.append(i)
            logging.info("the returned list after the operation is ", l3 )
            return l3
        except Exception as e:
            logging.exception("the exception that we have got is" + "\n" + str(e))
listobj = Get_all_lists()
listobj.extract_lists_in_given_list([3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}])