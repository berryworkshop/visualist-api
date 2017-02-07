CREATE
    // sources (external media)
    (visualist_v1:Source {
        name: 'The Visualist, version 1',
        type: 'website',
        version: 1,
        active: false,
        start: '2007',
        end: '2017'
        }),
    (visualist:Source {
        name: 'The Visualist',
        type: 'website',
        version: 2,
        start: '2017'
        }),
    (visualist)-[:SUCCESSOR_TO]->(visualist_v1),
    (visualist_desc:Description {
        body: 'The Visualist highlights the work of cultural producers such as, artists, makers, and curators that are central to your programming. While the Visualist is significant as a week to week destination for upcoming exhibitions, talks, and performances it is intended to function as a collective document of our communities efficacy and our shared identity as cultural producers in this place.\nThe Visualist follows On The Make, a calendar project that was developed by Karly Wildenhaus. It was then re-imagined and further developed by Jenny Kendler, Chad Kouri, and Steve Ruiz. The Visualist is currently being administered by Culture/Math, a jumble of fun loving team players that don’t believe in business cards. If you have any questions or suggestions, let us know at events@thevisualist.org.'
        }),
    (visualist_desc)-[:CITED_FROM {
        url: 'http://www.thevisualist.org/about/',
        accessed: '2017-02-06T03:47:07+00:00'
        }]->(visualist_v1),
    (visualist)-[:HAS_META]->(visualist_desc),

    // people
    (berry:Person {
        first_name: 'Allan',
        last_name: 'Berry',
        date_birth: '1977-05-23'}),
    (berry_address:Address {
        type: 'home',
        street: '913 W. Cullerton\nApt. 1',
        city: 'Chicago',
        state_province: 'Illinois',
        postal_code: '60608'
        }),
    (berry_phone:Phone {
        type: 'personal',
        country: '+1',
        area: '312',
        exchange: '371',
        number: '8722'
        }),
    (berry_email:Email {
        type: 'personal',
        email: 'allan.berry@gmail.com'
        }),
    (berry_desc:Description {
        body: 'Allan is an artist and librarian living in Chicago.'
        }),
    (berry)-[:HAS_META]->(berry_address),
    (berry)-[:HAS_META]->(berry_phone),
    (berry)-[:HAS_META]->(berry_email),
    (berry)-[:HAS_META]->(berry_desc),

    (duguid:Person {first_name: 'Meg', last_name: 'Meg'}),
    (thomas:Person {first_name: 'Michael', last_name: 'Thomas'}),

    (hampel:Person {first_name: 'Kate', last_name: 'Hampel'}),
    (hampel_desc:Description {
        body: 'Kate Hampel holds an MFA in Fiber and Material Studies from the School of the Art Institute of Chicago and a BFA from Concordia University in Montreal. Based in Chicago, she has participated in residencies across the United States, including the Vermont Studio Center, Arrowmont School of Arts and Crafts, and the Ragdale Foundation, and was the recipient of the Fountainhead Fellowship in Craft/Material Studies at Virginia Commonwealth University. Her work has been featured in the New York Times and has been shown nationally and internationally at galleries and museums including AIR Gallery in Brooklyn, NY; the Daegu Culture and Arts Center in South Korea; the Michigan Institute for Contemporary Art; and the Hudson Valley Center for Contemporary Art.'
        }),
    (hampel)-[:HAS_META]->(hampel_desc),
    (hampel_desc)-[:CITED_FROM {
        url: 'http://www.thevisualist.org/2017/02/kate-hampel-high-water/',
        accessed: '2017-02-06T03:47:07+00:00',
        rights: 'fair use'
        }]->(visualist_v1),

    (pollasch:Person {first_name: 'Kate', last_name: 'Pollasch'}),
    (pollasch_desc:Description {
        body: 'As a curator, art historian, and writer, Kate Pollasch’s practice interrogates pre-existing notions of history and normativity through queer tactics, network theory, archival studies, and considerations of affect and digital pedagogy. In 2012, she curated the exhibition “Roger Brown: This Boy’s Own Story” of Chicago Imagist artist Roger Brown, which unearthed previously censored artworks and archival materials from Brown’s career and resulted in Brown’s induction into the Visual AIDS Artist Registry. Pollasch holds a MA in Modern art History and Theory and an MA in Arts Administration and Cultural Policy from The School of the Art Institute of Chicago. She has held positions with The American Visionary Art Museum, The Art institute of Chicago, the Roger Brown House Museum, Sullivan Galleries, and most recently Rhona Hoffman Gallery. She has lectured at The Chicago History Museum, The Art Institute of Chicago, and The University of Chicago and is a contributing writer for New City, The Seen, and Elite Daily. Kate Pollasch was a 2015-2016 HATCH Projects Curatorial Resident with the Chicago Artists Coalition.'
        }),
    (pollasch)-[:HAS_META]->(pollasch_desc),
    (pollasch_desc)-[:CITED_FROM {
        url: 'http://www.thevisualist.org/2017/02/kate-hampel-high-water/',
        accessed: '2017-02-06T03:47:07+00:00',
        rights: 'fair use'
        }]->(visualist_v1),

    // organizations
    (caa:Organization {name: 'Chicago Artists Coalition'}),
    (caa_address:Address {
        private: false,
        street: '217 N Carpenter St.',
        city: 'Chicago',
        state_province: 'Illinois', 
        postal_code: '60607'
        }),
    (caa)-[:LOCATED_AT]->(caa_address),
    (terrain:Organization:Place {name: 'Terrain Exhibitions'}),
    (terrain_address:Address {
        private: false,
        street: '704 Highland Ave.',
        city: 'Oak Park',
        state_province: 'Illinois',
        postal_code: '60304'
        }),
    (terrain)-[:LOCATED_AT]->(terrain_address),
    
    // programs
    (hatch_residency:Event:Program {
        name: 'HATCH Public Art Residency'}),

    // events
    (high_water:Event:Exhibition {
        name: 'High Water',
        start: '2017-02-05T14:00:00-05:00',
        end: '2017-03-12'}),
    (hw_opening:Event:Reception {
        name: 'Hatch Opening',
        type: 'opening',
        start: '2017-02-05T14',
        end: 'T17'}),

    // relations
    (hampel)-[:CREATOR_OF {year:2017}]->(high_water),
    (pollasch)-[:CURATOR_OF]->(high_water),
    (caa)-[:PRODUCER_OF]->(hatch_residency),
    (terrain)-[:PRODUCER_OF]->(high_water)-[:AT]->(terrain),
    (caa)-[:PRODUCER_OF]->(high_water),

    (hw_opening)-[:AT]->(terrain),
    (hw_opening)-[:SUBEVENT_OF]->(hw_exhibition)

CREATE
    (uc:Organization:School {name: 'The University of Chicago'}),
    (uic:Organization:School {name: 'The University of Illinois at Chicago'}),
    (loyola:Organization:School {name: 'Loyola University Chicago'}),
    (depaul:Organization:School {name: 'DePaul University'}),
    (aic:Organization:Museum {name: 'The Art Institute of Chicago'}),
    (saic:Organization:School {name: 'The School of the Art Institute of Chicago'})-[:DEPARTMENT_OF]->(aic),
    (crawford:Person {first_name: 'Romi', last_name: 'Crawford'}),
    (crawford_desc:Description {
        body: 'Romi Crawford, Ph.D. is Associate Professor in Visual and Critical Studies and Liberal Arts at the School of the Art Institute of Chicago. Her research revolves primarily around formations of racial and gendered identity and the relation to American film, visual arts, and popular culture. She was previously the Curator and Director of Education and Public Programs at the Studio Museum in Harlem and founder of the Crawford and Sloan Gallery (NYC, 1994-1998). Her publications include writings in Art Journal; Cinema Remixed and Reloaded: Black Women Film and Video Artists (University of Washington, 2008); Black Light/White Noise: Sound and Light in Contemporary Art (Contemporary Art Contemporary Art Museum Houston, 2007); Frequency (Studio Museum in Harlem, 2006); Art and Social Justice Education: Culture as Commons (Routledge, 2011) and Service Media (Green Lantern, 2013).'
        }),
    (crawford)-[:HAS_META]->(crawford_desc),
    (crawford_desc)-[:CITED_FROM {
        url: 'http://www.thevisualist.org/2017/02/romi-crawford-radical-relations/',
        accessed: '2017-03-06T03:47:07+00:00'
        }]->(visualist_v1),

    (center:Organization {name: 'Center for the Study of Race, Politics and Culture'})-[:DEPARTMENT_OF]->(uc),
    (center_address:Address {
        private: false,
        street: '5733 S University Ave.',
        city: 'Chicago',
        state_province: 'Illinois', 
        postal_code: '60637'
        }),
    (center)-[:LOCATED_AT]->(center_address),

    (radical:Event:Exhibition {
        title: 'Radical Relations!',
        subtitle: 'Memory, Objects and the Generation of the Political',
        by_appointment: false,
        entrance_fee: 0
        }),
    (radical_desc:Description {
        body: 'On February 6, an exhibit exploring black liberation politics on the South Side of Chicago from 1967-2017 will open at The Center for the Study of Gender and Sexuality (CSGS). Curated by Romi Crawford, Associate Professor at the School of the Art Institute, this exhibit will display images of black artists, poets, writers, educators, and political organizers in everyday life, as well as display their personal communicative and decorative materials that have now become memorabilia, traces of a generation’s cultivation of radical care, a will to make social change felt at the level of their communal, familial, and intimate relations.'
        }),
    (radical)-[:HAS_META]->(radical_desc),
    (radical_desc)-[:CITED_FROM {
        url: 'http://www.thevisualist.org/2017/02/romi-crawford-radical-relations/',
        accessed: '2017-03-06T03:47:07+00:00'
        }]->(visualist_v1),
    (radical_opening:Event:Reception {
        type: 'opening',
        start: '2017-02-06T16:3018:30',
        end: 'T17'}),
    (radical_opening)-[:SUBEVENT_OF]->(radical),

    (center)-[:PRODUCER_OF]->(care:Series {name: 'Care@Chicago'}),
    (radical)-[:PART_OF]->(care),

    (crawford)-[:CURATOR_OF]->(radical),
    (saic)-[:EMPLOYER_OF {title: 'Associate Professor'}]->(crawford)

MATCH   (p1:Person {last_name: 'Meg'}),
        (p2:Person {last_name: 'Thomas'}),
        (p3:Person {last_name: 'Berry'}),
        (v1:Source {name: 'The Visualist, version 1'}),
        (v2:Source {name: 'The Visualist'})
CREATE  (o1:Organization {name: 'Culture/Math'}),
        (o2:Organization {name: 'Berry Catalog Workshop'}),
        (p1)-[:MEMBER_OF {role: 'owner'}]->(o1),
        (p2)-[:MEMBER_OF {role: 'owner'}]->(o1),
        (p3)-[:MEMBER_OF {role: 'owner'}]->(o2),
        (o1)-[:MANAGER_OF]->(v1),
        (o1)-[:MANAGER_OF]->(v2),
        (o2)-[:CREATOR_OF]->(v2)