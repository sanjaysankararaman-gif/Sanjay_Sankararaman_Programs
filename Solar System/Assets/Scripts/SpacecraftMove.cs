using UnityEngine;
using UnityEngine.InputSystem;

public class SpacecraftMove : MonoBehaviour
{
    public float speed = 5f;            // world units per second
    public float rotationSpeed = 90f;   // degrees per second

    // Right thumbstick for X (Left/Right) and Z (Forward/Backward)
    public InputAction thrust = new InputAction("Thrust", InputActionType.Value, "<XRController>{RightHand}/{Primary2DAxis}");

    // Left thumbstick for Y (Up/Down)
    public InputAction verticalThrust = new InputAction("VerticalThrust", InputActionType.Value, "<XRController>{LeftHand}/{Primary2DAxis}");

    void OnEnable()
    {
        thrust.Enable();
        verticalThrust.Enable();
    }

    void OnDisable()
    {
        thrust.Disable();
        verticalThrust.Disable();
    }

    void Update()
    {
        // Right thumbstick: x = strafe right, y = push forward
        Vector2 horizontalInput = thrust.ReadValue<Vector2>();
        float right = horizontalInput.x;    // X-axis
        float forward = horizontalInput.y;  // Z-axis

        // Left thumbstick: y = up/down
        float up = verticalThrust.ReadValue<Vector2>().y;  // Y-axis

        float rotateY = 0f;

        Keyboard kb = Keyboard.current;
        if (kb != null)
        {
            // Forward/Backward (Z)
            if (kb.upArrowKey.isPressed)    forward += 1f;
            if (kb.downArrowKey.isPressed)  forward -= 1f;

            // Left/Right strafe (X)
            if (kb.rightArrowKey.isPressed) right += 1f;
            if (kb.leftArrowKey.isPressed)  right -= 1f;

            // Up/Down (Y)
            if (kb.periodKey.isPressed)     up += 1f;   // . = up
            if (kb.commaKey.isPressed)      up -= 1f;   // , = down

            // Rotation around X axis
            if (kb.rightBracketKey.isPressed) rotateY += 1f;   // ] = positive
            if (kb.leftBracketKey.isPressed)  rotateY -= 1f;   // [ = negative
        }

        // Clamp individual axes so controller and keyboard inputs don't stack
        forward = Mathf.Clamp(forward, -1f, 1f);
        right = Mathf.Clamp(right, -1f, 1f);
        up = Mathf.Clamp(up, -1f, 1f);
        rotateY = Mathf.Clamp(-1f, rotateY, 1f);

        // Rotate first so movement uses the updated orientation
        transform.Rotate(0f, rotateY * rotationSpeed * Time.deltaTime, 0f, Space.Self);

        // Combine inputs using the spacecraft's local axes
        Vector3 moveDirection = (transform.forward * forward) + (transform.right * right) + (transform.up * up);

        // Clamp magnitude so diagonal movement isn't faster
        moveDirection = Vector3.ClampMagnitude(moveDirection, 1f);

        transform.position += moveDirection * speed * Time.deltaTime;
    }
}