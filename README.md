# Archdaily

[ArchDaily](https://www.archdaily.com/) is a weblog covering architectural news, projects,products, events, interviews and competitions, opinion pieces, among others, catering to architects, designers and other interested parties.

![](https://github.com/BahramJannesar/ArchdailyProjectDownloader/blob/master/image/logo.jpg)

## Idea 
I have too much architect friends, all of them whenever to want to find an idea about their project, first of all, check the Arcdaily website and tell me how can I download information and pictures of these projects, because of this I try to write this project for them but, I can't turn this project to usable product for architects. everyone does this job, It will be a great help to the community of architects .

## Dependencies

    pip install selenium
    pip install bs4
    pip install requests
   
   and must download the [chromedriver](https://chromedriver.chromium.org/) compatible with your chrome or [firefox driver](https://developer.mozilla.org/en-US/docs/Web/WebDriver) if you use firefox.
   
   **the path you must set the driver there is :** 
    /home/user/Desktop/ArchdailyProjectDownloader/driver/chromedriver
   
## Project detail

Every project in Arcdaily has the project id and you can find this from here 

![](https://github.com/BahramJannesar/ArchdailyProjectDownloader/blob/master/image/id.png)

Project deatails are download in .JSON file like this 

      {
    "Project ID": "939894",
    "Project Titel": "Zuidplein Theatre",
    "Project Type": "THEATER",
    "City": "ROTTERDAM",
    "Country": "THE NETHERLANDS",
    "Architects": "De Zwarte Hond",
    "Area": "12500 m²",
    "Year": "2020",
    "Photographs": "Scagliola Brakkee",
    "Project URL": "https://www.archdaily.com/939894",
    "Text Content": [
        "Text description provided by the architects. Zuidplein Theatre forms part of Hart van Zuid, a region-wide public-private partnership development focused around the Zuidplein and the Ahoy events complex. In cooperation with the city of Rotterdam, Ballast Nedam and Heijmans are constructing projects here such as the Rotterdam Ahoy Convention Centre, Zwemcentrum Rotterdam (swimming pool), an extension of the Zuidplein shopping centre, a new bus station, hotel, housing, and hospitality venues. The outdoor (public) spaces will also be completely redesigned. Following on from Zwemcentrum Rotterdam, Zuidplein Theatre is the second project completed in Hart van Zuid.",
   
        "Community role. Zuidplein Theatre replaces the adjacent former theatre which was built in 1953. When the new theatre is operational, the old building will be demolished in a circular way. This central location in the centre of Hart van Zuid, beside the bus and metro stations, easily attracts passersby to take a peek inside, making art and culture accessible to a wider audience.",
       
        "The library welcomes everyone from the community, offering a wide range of activities from languages to digital skills. Locals can meet here, learn, study, share experiences, and hold discussions. Young people are especially welcome. The theatre’s diverse programming often reflects what’s happening in the community, city, and region. Together with the café/restaurant, which is open every day, the complex plays an important role in the social fabric of Rotterdam-Zuid.",
        
        "Aluminium voile. Zuidplein Theatre has a clear, compact volume of approximately 12.500 m2. Due to noise considerations, the two auditoriums are positioned on the metro side, furthest away from the residential areas. Here, the building appears enclosed and intimate with a sturdy masonry facade accented by distinctive vertical niches. By contrast, a semi-transparent anodised aluminium veil drapes delicately over the entrance. The entrance area hosts the main public functions such as the library reading tables and the café/restaurant. By day, the semi-open facade creates a beautiful play of light inside, and by night, the facade illuminates from within to highlight the inviting entrance.",
       
        "The high lobby forms the heart of the building. Every function is directly or indirectly connected with this space, where there is always something for people to do and discover. As a ‘living room’ for Rotterdam-Zuid, the lobby has an extra stage that hosts popular activities such as children’s performances and other community-focused initiatives, bands and DJs and exhibitions.",
       
        "Designed by De Zwarte Hond in collaboration with BURO M2R, the interior fits seamlessly with the architecture. The transparency and curved form of the aluminium voile is reflected in various interior elements. The flexible and mobile bespoke furniture designed by BURO M2R enables spaces to be configured in different ways. Steel furniture and paneling lend the interior a bold look, while, at the same time, red upholstery and floors add the distinctive warmth of a theatre.",
        
        "Innovative theatre hall. The 600-seat main auditorium has two distinctive features. The Rotterdam-based architecture practice Studio RAP designed an acoustic wall that seemingly embraces the audience and performing artists in one fluid gesture. The design is crafted from 6000 different triangular aluminium composite panels – an unexpected choice of material for a theatre. Algorithms calculated the positioning of the triangular panels to create excellent acoustics in the theatre without the need for soundproofing materials.",
       
        "What’s also unique is how the auditorium adapts to standing concerts. Conventionally, a sliding tribune – which often has less comfortable seating – would be removed to make space for a standing event. At Zuidplein Theatre, the stage – whose surface area exceeds the hall – can easily be converted into a multipurpose space that fits a maximum of 1000 standing or dancing visitors. This means more comfortable fixed seating can be installed in the auditorium. The ground floor and balcony can be separated from the space using a moveable wall."
    ]
        }

and the project pictures are download in this directory.

## Licence

[MIT Licence](https://github.com/BahramJannesar/ArchdailyProjectDownloader/blob/master/LICENSE) 
