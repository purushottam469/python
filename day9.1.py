class ward:
      institution= None
      location=None

      def __init__(self,institution,location): # dunden method  # yo constructior jaba object initilize garxam taba call hunxa. 
            self.institution = institution
            self.location =location

            
      def get_institution(self):
            return self.institution
      def get_location(self):
            return self.location
      
      pass

district=ward('afdawd','acavv')    

district.get_institution()



print(district.institution)
print(district.location)
     
