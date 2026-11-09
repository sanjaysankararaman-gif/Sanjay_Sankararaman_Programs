using UnityEngine;

public class AimAtTarget : MonoBehaviour
{
    public Transform target;        // the Galaxy object
    public bool aimOnStart = true;  // also aims when you press Play

    void Start()
    {
        if (aimOnStart) Aim();
    }

    [ContextMenu("Aim At Target")]
    void Aim()
    {
        if (target == null) { Debug.LogWarning("AimAtTarget: no target assigned"); return; }
        transform.LookAt(target);
    }

    void OnDrawGizmosSelected()
    {
        Gizmos.color = Color.green;                       // where the ship's forward points
        Gizmos.DrawRay(transform.position, transform.forward * 100f);
        if (target != null)
        {
            Gizmos.color = Color.red;                     // the line to the target
            Gizmos.DrawLine(transform.position, target.position);
        }
    }
}