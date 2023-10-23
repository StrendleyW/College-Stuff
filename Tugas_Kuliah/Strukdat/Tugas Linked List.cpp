#include <iostream>
using namespace std;
struct Mahasiswa{
    string nama, npm;
    int usia;
    Mahasiswa *next;
};
Mahasiswa *head, *tail, *cur, *newNode, *del;
void createSLL(string nama, string npm, int usia){
    head = new Mahasiswa();
    head->nama = nama;
    head->npm = npm;
    head->usia = usia;
    head->next = NULL;
    tail = head;
}
void addFirst(string nama, string npm, int usia){
    newNode = new Mahasiswa();
    newNode->nama = nama;
    newNode->npm = npm;
    newNode->usia = usia;
    newNode->next = head;
    head = newNode;
}
void addMiddle(string nama, string npm, int usia){
    newNode = new Mahasiswa();
    newNode->nama = nama;
    newNode->npm = npm;
    newNode->usia = usia;
    newNode->next = NULL;

    Mahasiswa *fast = head; //fast bergerak 2 langkah
    Mahasiswa *slow = head; //slow bergerak 1 langkah
    Mahasiswa *prev = NULL; //prev mengikuti slow

    while (fast != NULL && fast->next != NULL) {
        fast = fast->next->next; // 2 langkah
        prev = slow; // slow mengikuti prev
        slow = slow->next; // 1 langkah
    }

    if (prev == NULL) { //mengecek apakah linked list sudah kosong
        head = newNode; // Tambahkan newNode sebagai head.
        tail = newNode;
    } else {
        // Tambahkan newNode setelah elemen prev.
        prev->next = newNode;
        newNode->next = slow;
    }
}
void addLast(string nama, string npm, int usia){
    newNode = new Mahasiswa();
    newNode->nama = nama;
    newNode->npm = npm;
    newNode->usia = usia;
    newNode->next = NULL;
    tail->next = newNode;
    tail = newNode;
}
void changeFirst(string nama, string npm, int usia){
    head->nama = nama;
    head->npm = npm;
    head->usia = usia;
}
void changeMiddle(string nama, string npm, int usia) {
    Mahasiswa *slow = head; // fast bergerak 2 langkah
    Mahasiswa *fast = head; // slow bergerak 1 langkah
    Mahasiswa *prev = NULL; // prev mengikuti slow samapi linklist habis

    while (fast != NULL && fast->next != NULL) {
        slow = slow->next; // 1 langkah
        fast = fast->next->next; // 2 langkah
        prev = slow; // prev mengikuti slow
    }

    slow->nama = nama; // mengubah nilai tengahnya
    slow->npm = npm;
    slow->usia = usia;
}
void changeLast(string nama, string npm, int usia){
    tail->nama = nama;
    tail->npm = npm;
    tail->usia = usia;
}
void deleteFirst(){
    del = head;
    head = head->next;
    delete del;
}
void deleteMiddle() {
    Mahasiswa *slow = head; // fast bergerak 2 langkah
    Mahasiswa *fast = head; // slow bergerak 1 langkah
    Mahasiswa *prev = NULL; // prev mengikuti slow sampai linklist habis

    while (fast != NULL && fast->next != NULL) {
        fast = fast->next->next; // 2 langkah
        prev = slow; // prev mengikuti slow
        slow = slow->next; // 1 langkah
    }

    prev->next = slow->next; // mengubah pointer prev->next ke elemen tengah yang akan dihapus
    delete slow; // menghapus elemen tengah
}
void deleteLast(){
    del = tail;
    cur = head;
    while (cur->next != tail){
        cur = cur->next;
    }
    tail = cur;
    tail->next = NULL;
    delete del;
}


void cetakSLL(){
    cur = head;
    while(cur != NULL){
        cout << "Nama Mhs : " << cur->nama << endl;
        cout << "NPM Mhs : " << cur->npm << endl;
        cout << "Usia Mhs : " << cur->usia << endl;
        cur = cur->next;
    }
}

int main() {
    createSLL("Yusron", "2008180004", 20);
    addFirst("Sarah1", "2008180014", 17);
    addMiddle("Vendy1", "2008180024", 18);
    addLast("Doni", "2008180009", 20);
    cetakSLL();
    cout << "\n";
    changeFirst("Budi", "22081010328", 19);
    changeMiddle("Putri", "2008180034", 18);
    changeLast("Sandy", "2008180044", 18);
    cetakSLL();
    cout << "\n";
    deleteFirst();
    deleteMiddle();
    deleteLast();
    cetakSLL();
    cout << "\n";
}
