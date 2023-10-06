Algorithm Calculat_Average_And_Appreciation
Variables
    N1, N2, N3, M: Real

Begin
    Write("Enter grade 1: ")
    Read(N1)
    While N1 > 20 OR N1 < 0
        Write("Please enter a correct grade for N1: ")
        Read(N1)

    Write("Enter grade 2: ")
    Read(N2)
    While N2 > 20 OR N2 < 0
        Write("Please enter a correct grade for N2: ")
        Read(N2)

    Write("Enter grade 3: ")
    Read(N3)
    While N3 > 20 OR N3 < 0
        Write("Please enter a correct grade for N3: ")
        Read(N3)

    M ← (N1 + N2 + N3) / 3
    Write("The average of the grades is: ", M)
    if M > 16 Then
        Write("EXCELLENT")
    Elif 14 <= M < 16 Then
        Write("GOOD")
    Elif 12 <= M < 14 Then
        Write("SATISFACTORY")
    Elif 10 <= M < 12 Then
        Write("PASS")
    Else
        Write("FAIL")
    End if

End
