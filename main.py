import requests

url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"

headers = {
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
    'x-rapidapi-key': "d89543b6c5mshea6df840b5d3bfdp1739cfjsnc402d948eca9"
    }

response = requests.request("GET", url, headers=headers).json()
try:
  def searchByState(statename):
    try:
      for state in response['state_wise']:
        if int(response['state_wise'][state]['active']) != 0:
            if state == statename: 
              return { 'active_cases': response['state_wise'][state]['active'], 'deceased_cases' : response['state_wise'][state]['deaths'] ,'recovered_cases' : response['state_wise'][state]['recovered']}
    except NameError:
        return None

  if __name__ == '__main__':  
    output=""
    statename = input("Enter the state name : ")
    statename = statename.title()

    case = searchByState(statename)
    if case != None:
      output += str(statename) + ": " + str(case)
      print(output)
    else:
      print("Please enter correct State Name with proper spacing. ")

        
except ValueError:
  print("No Data Found...")
  
    
    
    
    