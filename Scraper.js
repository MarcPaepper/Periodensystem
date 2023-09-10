// import fs
import fs from 'fs';

// const nameList = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen"];
const nameList = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminium', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', 'Potassium', 'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', 'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc', 'Gallium', 'Germanium', 'Arsenic', 'Selenium', 'Bromine', 'Krypton', 'Rubidium', 'Strontium', 'Yttrium', 'Zirconium', 'Niobium', 'Molybdenum', 'Technetium', 'Ruthenium', 'Rhodium', 'Palladium', 'Silver', 'Cadmium', 'Indium', 'Tin', 'Antimony', 'Tellurium', 'Iodine', 'Xenon', 'Caesium', 'Barium',
    'Lanthanum', 'Cerium', 'Praseodymium', 'Neodymium', 'Promethium', 'Samarium', 'Europium', 'Gadolinium', 'Terbium', 'Dysprosium', 'Holmium', 'Erbium', 'Thulium', 'Ytterbium', 'Lutetium', 'Hafnium', 'Tantalum', 'Tungsten', 'Rhenium', 'Osmium', 'Iridium', 'Platinum', 'Gold', 'Mercury', 'Thallium', 'Lead', 'Bismuth', 'Polonium', 'Astatine', 'Radon', 'Francium', 'Radium', 'Actinium', 'Thorium', 'Protactinium', 'Uranium', 'Neptunium', 'Plutonium', 'Americium', 'Curium', 'Berkelium', 'Californium', 'Einsteinium',
    'Fermium', 'Mendelevium', 'Nobelium', 'Lawrencium', 'Rutherfordium', 'Dubnium', 'Seaborgium', 'Bohrium', 'Hassium', 'Meitnerium', 'Darmstadtium', 'Roentgenium', 'Copernicium', 'Nihonium', 'Flerovium', 'Moscovium', 'Livermorium', 'Tennessine', 'Oganesson']

// Define an array to store the results
const results = [];

// Define an async function to sequentially retrieve lengths
async function retrieveLengthsSequentially() {
    for (const name of nameList) {
        try {
            const length = await getPageViews(name);
            results.push({ name, length });
        } catch (error) {
            console.error(`Error fetching length for ${name}: ${error.message}`);
        }
    }

    // Zip the nameList and results into a dictionary
    const jsonData = {};
    for (const item of results) {
        jsonData[item.name] = item.length;
    }

    // save to output file Output/Wikilengths.json
    
    fs.writeFileSync('Output/Wikilengths.json', JSON.stringify(jsonData, null, 2), 'utf-8');
    
    console.log('Data has been saved');

    // All requests are done, you can now work with the zippedData dictionary
    console.log(jsonData);
}

// Call the function to start the sequential retrieval
retrieveLengthsSequentially();

async function getPageViews(name) {
    // const apiUrl = `https://en.wikipedia.org/w/api.php?action=query&format=json&titles=${name}&prop=revisions&rvprop=size`;
    const apiUrl = `https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/${name}/daily/20220101/20221231`;

    try {
        const response = await fetch(apiUrl);

        if (response.status !== 200) {
            throw new Error(`Request failed with status ${response.status}`);
        }

        const data = await response.json();
        
        const views = data.items[0].views;
        return views;
        // const page = data.query.pages[Object.keys(data.query.pages)[0]];
        // const revision = page.revisions[0];
        // const length = revision.size;

        // return length; // This will resolve the promise with the length value.
    } catch (error) {
        throw error; // This will propagate the error to the caller.
    }
}