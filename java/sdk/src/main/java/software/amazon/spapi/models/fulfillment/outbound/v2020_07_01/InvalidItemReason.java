/*
 * Selling Partner APIs for Fulfillment Outbound
 * The Selling Partner API for Fulfillment Outbound lets you create applications that help a seller fulfill Multi-Channel Fulfillment orders using their inventory in Amazon's fulfillment network. You can get information on both potential and existing fulfillment orders.
 *
 * OpenAPI spec version: 2020-07-01
 *
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

package software.amazon.spapi.models.fulfillment.outbound.v2020_07_01;

import com.google.gson.annotations.SerializedName;
import io.swagger.v3.oas.annotations.media.Schema;
import java.util.Objects;

/** The reason that the item is invalid for return. */
@Schema(description = "The reason that the item is invalid for return.")
public class InvalidItemReason {
    @SerializedName("invalidItemReasonCode")
    private InvalidItemReasonCode invalidItemReasonCode = null;

    @SerializedName("description")
    private String description = null;

    public InvalidItemReason invalidItemReasonCode(InvalidItemReasonCode invalidItemReasonCode) {
        this.invalidItemReasonCode = invalidItemReasonCode;
        return this;
    }

    /**
     * Get invalidItemReasonCode
     *
     * @return invalidItemReasonCode
     */
    @Schema(required = true, description = "")
    public InvalidItemReasonCode getInvalidItemReasonCode() {
        return invalidItemReasonCode;
    }

    public void setInvalidItemReasonCode(InvalidItemReasonCode invalidItemReasonCode) {
        this.invalidItemReasonCode = invalidItemReasonCode;
    }

    public InvalidItemReason description(String description) {
        this.description = description;
        return this;
    }

    /**
     * A human readable description of the invalid item reason code.
     *
     * @return description
     */
    @Schema(required = true, description = "A human readable description of the invalid item reason code.")
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    @Override
    public boolean equals(java.lang.Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        InvalidItemReason invalidItemReason = (InvalidItemReason) o;
        return Objects.equals(this.invalidItemReasonCode, invalidItemReason.invalidItemReasonCode)
                && Objects.equals(this.description, invalidItemReason.description);
    }

    @Override
    public int hashCode() {
        return Objects.hash(invalidItemReasonCode, description);
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("class InvalidItemReason {\n");

        sb.append("    invalidItemReasonCode: ")
                .append(toIndentedString(invalidItemReasonCode))
                .append("\n");
        sb.append("    description: ").append(toIndentedString(description)).append("\n");
        sb.append("}");
        return sb.toString();
    }

    /** Convert the given object to string with each line indented by 4 spaces (except the first line). */
    private String toIndentedString(java.lang.Object o) {
        if (o == null) {
            return "null";
        }
        return o.toString().replace("\n", "\n    ");
    }
}
