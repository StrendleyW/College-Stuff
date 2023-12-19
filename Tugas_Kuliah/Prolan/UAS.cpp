#include <iostream>
#include <iomanip>

using namespace std;

// Struct for storing data on the number of PNS based on gender and job position
struct JumlahPNSJenisJabatan {
    string jabatanpns;
    int jumlahPriaPNS;
    int jumlahWanitaPNS;
    float persentotalkelaminPNS;
    float persenPriaPNS;
    float persenWanitaPNS;
    float jumlahpersenPNS;
};

// Struct for storing data on the number of PNS based on functional position and gender
struct JumlahPNSJabatanFungsional {
    string jabatanFungsional;
    int jumlahPriaFungsi;
    int jumlahWanitaFungsi;
    float persentotalkelaminFungsi;
    float persenPriaFungsi;
    float persenWanitaFungsi;
    float jumlahpersenFungsi;
};

int main() {
    // Sample data initialization
    const int jumlahDataJenisJabatan = 8;
    JumlahPNSJenisJabatan dataJenisJabatan[jumlahDataJenisJabatan] = {
        {"Fungsional Umum", 0, 0, 0, 0, 0},
        {"Fungsional Tertentu", 0, 0, 0, 0, 0},
        {"Struktural", 0, 0, 0, 0, 0},
        {"Eselon 1", 0, 0, 0, 0, 0},
        {"Eselon 2", 0, 0, 0, 0, 0},
        {"Eselon 3", 0, 0, 0, 0, 0},
        {"Eselon 4", 0, 0, 0, 0, 0},
        {"Eselon 5", 0, 0, 0, 0, 0}
    };

    const int jumlahDataJabatanFungsional = 5;
    JumlahPNSJabatanFungsional dataJabatanFungsional[jumlahDataJabatanFungsional] = {
        {"Tenaga Pendidik", 0, 0, 0, 0, 0},
        {"Tenaga Medis", 0, 0, 0, 0, 0},
        {"Tenaga Paramedis", 0, 0, 0, 0, 0},
        {"Dosen", 0, 0, 0, 0, 0},
        {"Lainnya", 0, 0, 0, 0, 0}
    };

    // Initialize totalPria and totalWanita
    int totalPriaPNS = 0;
    int totalWanitaPNS = 0;
    float totalpersenpriapns = 0;
    float totalpersenwanitapns = 0;
    int finaltotalkelaminpns = 0;

    const int jumlahData = 13;
    JumlahPNSJenisJabatan datapns[jumlahData];

    cout << endl <<"---Tabel Jenis Jabatan PNS---" << endl;
    for (int i = 0; i < jumlahDataJenisJabatan; ++i) {
        cout << endl <<"//// " << dataJenisJabatan[i].jabatanpns << " ////" << endl;
        cout << "Masukkan jumlah Pria dan Wanita untuk data " << dataJenisJabatan[i].jabatanpns << ":\n";
        cout << "Jumlah Pria: ";
        cin >> datapns[i].jumlahPriaPNS;
        totalPriaPNS += datapns[i].jumlahPriaPNS;

        cout << "Jumlah Wanita: ";
        cin >> datapns[i].jumlahWanitaPNS;
        totalWanitaPNS += datapns[i].jumlahWanitaPNS;

        int totalkelaminpns = totalPriaPNS + totalWanitaPNS;
        finaltotalkelaminpns += totalkelaminpns;

        // Menghitung persentase
        datapns[i].persenPriaPNS = static_cast<float>(datapns[i].jumlahPriaPNS) / (datapns[i].jumlahPriaPNS + datapns[i].jumlahWanitaPNS) * 100;
        datapns[i].persenWanitaPNS = static_cast<float>(datapns[i].jumlahWanitaPNS) / (datapns[i].jumlahPriaPNS + datapns[i].jumlahWanitaPNS) * 100;
        datapns[i].persentotalkelaminPNS = static_cast<float>(datapns[i].jumlahPriaPNS + datapns[i].jumlahWanitaPNS) / (finaltotalkelaminpns) * 100;
    }

    // Calculate the total for each position
    int totalkelaminpns[jumlahDataJenisJabatan];
    for (int i = 0; i < jumlahDataJenisJabatan; ++i) {
        totalkelaminpns[i] = datapns[i].jumlahPriaPNS + datapns[i].jumlahWanitaPNS;
    }

    // Calculate the percentage for each position
    float persentotalkelaminPNS[jumlahDataJenisJabatan];
    for (int i = 0; i < jumlahDataJenisJabatan; ++i) {
        persentotalkelaminPNS[i] = static_cast<float>(totalkelaminpns[i]) / (totalPriaPNS + totalWanitaPNS) * 100;
    }

    int totalPriafungsi = 0;
    int totalWanitafungsi = 0;
    float totalpersenpriafungsi = 0;
    float totalpersenwanitafungsi = 0;
    float finaltotalkelaminfungsi = 0;

    JumlahPNSJabatanFungsional datafungsi[jumlahData];

    cout << endl << "---Tabel Jabatan Fungsional---" << endl;

    for (int i = 0; i < jumlahDataJabatanFungsional; ++i) {
        int totalkelaminfungsi = 0;
        cout << endl <<"//// " << dataJabatanFungsional[i].jabatanFungsional << " ////" << endl;
        cout << "Masukkan jumlah Pria dan Wanita untuk data " << dataJabatanFungsional[i].jabatanFungsional << ":\n";
        
        cout << "Jumlah Pria: ";
        cin >> datafungsi[i].jumlahPriaFungsi;
        totalPriafungsi += datafungsi[i].jumlahPriaFungsi;

        cout << "Jumlah Wanita: ";
        cin >> datafungsi[i].jumlahWanitaFungsi;
        totalWanitafungsi += datafungsi[i].jumlahWanitaFungsi;

        totalkelaminfungsi = totalPriafungsi + totalWanitafungsi;
        finaltotalkelaminfungsi += totalkelaminfungsi;

        // Menghitung persentase
        datafungsi[i].persenPriaFungsi = static_cast<float>(datafungsi[i].jumlahPriaFungsi) / (datapns[i].jumlahPriaPNS + datapns[i].jumlahWanitaPNS) * 100;
        datafungsi[i].persentotalkelaminFungsi = static_cast<float>(datafungsi[i].jumlahPriaFungsi + datafungsi[i].jumlahWanitaFungsi) / finaltotalkelaminfungsi * 100;
        
        // Corrected parentheses in the following line
        datafungsi[i].persenWanitaFungsi = static_cast<float>(datafungsi[i].jumlahWanitaFungsi) / (datapns[i].jumlahPriaPNS + datapns[i].jumlahWanitaPNS) * 100;
    }

    // Calculate the total for each position
    int totalkelaminfungsi[jumlahDataJabatanFungsional];
    for (int i = 0; i < jumlahDataJabatanFungsional; ++i) {
        totalkelaminfungsi[i] = datafungsi[i].jumlahPriaFungsi + datafungsi[i].jumlahWanitaFungsi;
    }

    // Calculate the percentage for each position
    float persentotalkelaminfungsi[jumlahDataJabatanFungsional];
    for (int i = 0; i < jumlahDataJabatanFungsional; ++i) {
        persentotalkelaminfungsi[i] = static_cast<float>(totalkelaminfungsi[i]) / (totalPriafungsi + totalWanitafungsi) * 100;
    }

    // Menggunakan variabel total untuk menghitung jumlah jabatan PNS dan fungsional secara keseluruhan
    int totalPNS = totalPriaPNS + totalWanitaPNS;
    int totalfungsi = totalPriafungsi + totalWanitafungsi;

    cout << "Total Jenis Jabatan PNS (Pria + Wanita): " << totalPNS << endl;
    cout << "Total Jabatan Fungsional (Pria + Wanita): " << totalfungsi << endl;

    
    // Menampilkan hasil persentase untuk setiap jabatan (Tabel Jenis Jabatan)
    for (int i = 0; i < jumlahDataJenisJabatan; ++i) {
        cout << "//// " << dataJenisJabatan[i].jabatanpns << " ////" << endl;
        cout << "Persentase Pria: " << datapns[i].persenPriaPNS << "%" << endl;
        cout << "Persentase Wanita: " << datapns[i].persenWanitaPNS << "%" << endl << endl;
        totalpersenpriapns += datapns[i].persenPriaPNS;
        totalpersenwanitapns += datapns[i].persenWanitaPNS;
        cout << "Total Persen Jumlah banyak PNS untuk jenis jabatan " << dataJenisJabatan[i].jabatanpns << " = " << persentotalkelaminPNS[i] << "%" <<endl;
    }

    float finaltotalpersenpns = totalpersenpriapns + totalpersenwanitapns;
    cout << "Total Seluruh Persen PNS jenis jabatan :" << finaltotalpersenpns << endl;

    // Menampilkan hasil persentase untuk setiap jabatan (Tabel Jabatan Fungsional)
    for (int i = 0; i < jumlahDataJabatanFungsional; ++i) {
        cout << "//// " << dataJabatanFungsional[i].jabatanFungsional << " ////" << endl;
        cout << "Persentase Pria: " << datafungsi[i].persenPriaFungsi << "%" << endl;
        cout << "Persentase Wanita: " << datafungsi[i].persenWanitaFungsi << "%" << endl << endl;
        totalpersenpriafungsi += datafungsi[i].persenPriaFungsi;
        totalpersenwanitafungsi += datafungsi[i].persenWanitaFungsi;
        cout << "Total Persen Jumlah banyak PNS untuk jabatan fungsional " << dataJabatanFungsional[i].jabatanFungsional << " = " << persentotalkelaminfungsi[i] << "%" << endl;
    }

    float finaltotalpersenfungsi = totalpersenpriafungsi + totalpersenwanitafungsi;
    cout << "Total Seluruh Persen PNS jabatan fungsional :" << finaltotalpersenfungsi << endl;


    //Save data to console (Jenis Jabatan)
    cout << endl << "=== Persentase Jenis Jabatan ===" << endl;
    cout << left << setw(20) << "Jenis Jabatan" << setw(10) << "Pria" << setw(10) << "Wanita" << setw(15) << "Persen Pria" << setw(15) << "Persen Wanita" << setw(20) << "Jumlah" << setw(15) << "Persen Jumlah" << endl;
    for (int i = 0; i < jumlahDataJenisJabatan; ++i) {
        cout << left << setw(20) << dataJenisJabatan[i].jabatanpns<< setw(10) << datapns[i].jumlahPriaPNS << setw(10) << datapns[i].jumlahWanitaPNS
             << setw(15) << fixed << setprecision(2) << datapns[i].persenPriaPNS << "%" << setw(15) << datapns[i].persenWanitaPNS << "%" << setw(20) << fixed << setprecision(2) << totalPNS << setw(20) << persentotalkelaminPNS[i] << "%" << endl;
    }


    //Save data to console (fungsional)
    cout << endl << "=== Persentase Jabatan Fungsional ===" << endl;
    cout << left << setw(20) << "Jabatan Fungsional" << setw(10) << "Pria" << setw(10) << "Wanita" << setw(15) << "Persen Pria" << setw(15) << "Persen Wanita" << setw(20) << "Jumlah" << setw(15) << "Persen Jumlah" << endl;
    for (int i = 0; i < jumlahDataJabatanFungsional; ++i) {
        cout << left << setw(20) << dataJabatanFungsional[i].jabatanFungsional << setw(10) << datafungsi[i].jumlahPriaFungsi << setw(10) << datafungsi[i].jumlahWanitaFungsi
             << setw(15) << fixed << setprecision(2) << datafungsi[i].persenPriaFungsi << "%" << setw(15) << datafungsi[i].persenWanitaFungsi << "%" << setw(20) << fixed << setprecision(2) << totalfungsi << setw(20) << (datafungsi[i].jumlahPriaFungsi + datafungsi[i].jumlahWanitaFungsi) << setw(20) << persentotalkelaminfungsi[i] << "%" << endl;
    }



int maxPNS = 0;
string jabatanMaxPNS;

int i = 1;
while (i < jumlahDataJenisJabatan && totalkelaminpns[i] <= maxPNS) {
    i *= 2;
}

int left = i / 2;
int right = min(i, jumlahDataJenisJabatan - 1);

while (left <= right) {
    int mid = left + (right - left) / 2;

    if (totalkelaminpns[mid] > maxPNS) {
        maxPNS = totalkelaminpns[mid];
        jabatanMaxPNS = dataJenisJabatan[mid].jabatanpns;
    }

    if (totalkelaminpns[mid] == maxPNS) {
        break;  // Jika ada duplikasi, keluar dari loop
    } else if (totalkelaminpns[mid] < maxPNS) {
        left = mid + 1;
    } else {
        right = mid - 1;
    }
}

cout << "\nJenis jabatan dengan PNS terbanyak: " << jabatanMaxPNS << " (" << maxPNS << " PNS)" << endl;


    // Bubble sort functional positions based on total PNS in descending order
    for (int i = 0; i < jumlahDataJabatanFungsional - 1; ++i) {
        for (int j = 0; j < jumlahDataJabatanFungsional - i - 1; ++j) {
            int totalPNS1 = datafungsi[j].jumlahPriaFungsi + datafungsi[j].jumlahWanitaFungsi;
            int totalPNS2 = datafungsi[j + 1].jumlahPriaFungsi + datafungsi[j + 1].jumlahWanitaFungsi;

            if (totalPNS1 < totalPNS2) {
                // Swap datafungsi[j] and datafungsi[j + 1]
                swap(datafungsi[j], datafungsi[j + 1]);
            }
        }
    }

    // Display functional positions in descending order
    cout << "\n---Urutan Jabatan Fungsional dari Terbanyak---" << endl;
    for (int i = 0; i < jumlahDataJabatanFungsional; ++i) {
    cout << dataJabatanFungsional[i].jabatanFungsional << " - " << (datafungsi[i].jumlahPriaFungsi + datafungsi[i].jumlahWanitaFungsi) << " PNS" << endl;
    }
    
    return 0;

}
