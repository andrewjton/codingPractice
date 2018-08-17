// main.cpp, my_vector.hpp, my_vector.cpp
// $ c++
// clang++ main.cpp, my_vector.hpp, my_vector.cpp
// a.out
class my_vector {
  int *memLoc; #array pointer to arbitrary sized array
  int capacity;
  int numElems;

  my_vector() { //constructor
    // preallocate set size of memory
    int *memLoc = new int [8];
    capacity = 8;
    numElems = 0;
  }
  
  public void push_back(int val) {
    //check capacity
    //if it runs out of capacity:
    //    allocate more memory
    //
    if (numElems + 1 >= capacity) {
      reallocateMemory();
    }
    
    //2. find the nearest unused space in your array & update it w/ new val
    memLoc[numElems++] = val;
    return;
  }
  
  private void reallocateMemory() {
    capacity = 2 * capacity;
    memLoc2 = new int [2*capacity];
    //copy all of the original elements into the new array
    int i = 0;
    
    for (; i < capacity / 2; i++) {
      memLoc2[i] = memLoc[i];
    }
    
    //deallocate memLoc
    delete [] memLoc;
    
    memLoc = memLoc2;
  }
  
}

// do not modify anything below this line
int main() {
  my_vector a;
  a.push_back(42);
  a.push_back(7);
  // and so on...
  
  return 0;
}

// main.cpp, my_vector.hpp, my_vector.cpp
// $ c++