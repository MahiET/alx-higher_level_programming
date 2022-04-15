# 0x14. JavaScript - Web scraping

Working with JSON
=
JavaScript Object Notation (JSON) is a standard text-based format for representing structured data based on JavaScript object syntax. It is commonly used for transmitting data in web applications (e.g., sending some data from the server to the client, so it can be displayed on a web page, or vice versa). You'll come across it quite often, so in this article we give you all you need towork with JSON using JavaScript, including parsing JSON so you can access data within it, and creating JSON.

JSON structure
=

As described above, JSON is a string whose format very much resembles JavaScript object literal format. You can include the same basic data types inside JSON as you can in a standard object JavaScript strings, numbers, arrays, booleans, and other object literals. 

 {
     "squadName": "Super hero squad",

      "homeTown": "Metro City",

         "formed": 2016,

           "secretBase": "Super tower",

            "active": true,

                       "members": [
       {
       
         "name": "Molecule Man",
       
             "age": 29,
       
          "secretIdentity": "Dan Jukes",
        
             "powers": [
        
            "Radiation resistance",
        
                "Turning tiny",
       
                 "Radiation blast"
              ]
                  },
      {
      
           "name": "Madame Uppercut",
        
             "age": 39,
        
          "secretIdentity": "Jane Wilson",
        
           "powers": [
        
              "Million tonne punch",
        
              "Damage resistance",
        
              "Superhuman reflexes"
      
              ]
      
               },
        {

          "name": "Eternal Flame",
          
              "age": 1000000,
          
             "secretIdentity": "Unknown",
          
                 "powers": [
          
               "Immortality",
          
                 "Heat Immunity",
          
               "Inferno",
          
                 "Teleportation",
          
                    "Interdimensional travel"
               ]
             }
           ]
          } 