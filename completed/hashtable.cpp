/*
FEATURES (key=integer, value=string)
Open addressing (linear probing)
hashing fxn is a power of 37
Why is table size prime? --> reduces possible collisions if the tablesize & the hashing functions are coprime!

future implementation:
1. resize automatically if half full --> reduces collisions
2. quadratic probing --> more spread
3. implement delete (requires you to have sentinel values (easiest))
4. deleter method?
*/

//cstring vs. vector? vs array?

int main() {

	return 0;
}

class HashTable {
	int size;
	char * values; //point to  the actual values
	int * keys; //pointer to an array that stores what spaces in "values" are used by which keys.

	public hashTable() {
		this.size = 1024; //default size is a power of 2
		this.values = new char[size];
		this.keys = new int[size];
	}

	public int get(int key) {
		int h = hash(key);
		int id = findSpot(h, key, 'get');
		if (id == -1) return -1; //DNE

		return values[id];
	}

	public void put (int key, int val) {
		int h = hash(key);
		int id = findSpot(h, key, 'put');
		values[id] = val;
	}

	private int findSpot(int hash, int key, string purpose){
		if (purpose == 'get') {
			int id = hash;
			int counter = 0;
			while (keys[id] != key && counter < size) { //linear probing

				id = (id + 1) % size;
				counter++;
			}

			if (keys[id] != key) return -1; //means no value
			else return id;
		}
		else if (purpose == 'put') {
			int id = hash;
			int counter = 0;
			while (keys[id] != 0 && counter < size) {

				id = (id + 1) % size;
				counter++;
			}

			if (keys[id] == 0) {
				//resize
			}
			else return id;
		}

	}


}