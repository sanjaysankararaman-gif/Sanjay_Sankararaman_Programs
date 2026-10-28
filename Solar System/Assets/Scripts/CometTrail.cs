using UnityEngine;

public class CometTail : MonoBehaviour
{
    public Transform sun;
    public Transform comet;

    void Update()
    {
        // Direction pointing AWAY from the Sun, through the comet
        Vector3 awayFromSun = (comet.position - sun.position).normalized;

        // Position the tail at the comet, oriented to point away from the sun
        transform.position = comet.position;
        transform.rotation = Quaternion.LookRotation(awayFromSun);
    }
}